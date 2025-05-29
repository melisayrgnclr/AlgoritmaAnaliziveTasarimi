import sys
import random
import math
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton, QLabel,
                             QLineEdit, QVBoxLayout, QHBoxLayout, QSlider, QGraphicsScene,
                             QGraphicsView, QComboBox)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPen, QColor

# === Union-Find ===
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u == root_v:
            return False
        if self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v
        else:
            self.parent[root_v] = root_u
            if self.rank[root_u] == self.rank[root_v]:
                self.rank[root_u] += 1
        return True

# === Grafik Oluşturucu ===
def generate_random_graph(n, m):
    edges = set()
    for i in range(1, n):
        u = i - 1
        v = i
        w = random.randint(1, 50)
        edges.add((u, v, w))
    while len(edges) < m:
        u = random.randint(0, n - 1)
        v = random.randint(0, n - 1)
        if u != v:
            w = random.randint(1, 100)
            edges.add((min(u, v), max(u, v), w))
    return list(edges)

# === Kruskal ===
def kruskal_with_steps(n, edges):
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(n)
    mst_steps = []
    for u, v, w in edges:
        if uf.union(u, v):
            mst_steps.append((u, v, w))
            if len(mst_steps) == n - 1:
                break
    return mst_steps

# === Ana Arayüz ===
class KruskalVisualizer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kruskal Algoritması Görselleştirici")
        self.setGeometry(100, 100, 1200, 800)

        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)

        self.node_input = QLineEdit("200")
        self.edge_input = QLineEdit("1000")

        self.layout_choice = QComboBox()
        self.layout_choice.addItems(["Daire", "Grid"])

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(10)
        self.slider.setMaximum(1000)
        self.slider.setValue(200)

        self.info_label = QLabel("Bilgi kutusu")

        self.generate_btn = QPushButton("Graf Oluştur")
        self.start_btn = QPushButton("Başlat")
        self.stop_btn = QPushButton("Durdur")
        self.reset_btn = QPushButton("Sıfırla")

        self.generate_btn.clicked.connect(self.generate_graph)
        self.start_btn.clicked.connect(self.start_animation)
        self.stop_btn.clicked.connect(self.stop_animation)
        self.reset_btn.clicked.connect(self.reset_scene)

        layout = QVBoxLayout()
        controls = QHBoxLayout()

        controls.addWidget(QLabel("Düğüm:"))
        controls.addWidget(self.node_input)
        controls.addWidget(QLabel("Kenar:"))
        controls.addWidget(self.edge_input)
        controls.addWidget(QLabel("Düzen:"))
        controls.addWidget(self.layout_choice)
        controls.addWidget(QLabel("Hız:"))
        controls.addWidget(self.slider)
        controls.addWidget(self.generate_btn)
        controls.addWidget(self.start_btn)
        controls.addWidget(self.stop_btn)
        controls.addWidget(self.reset_btn)

        layout.addLayout(controls)
        layout.addWidget(self.view)
        layout.addWidget(self.info_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.positions = {}
        self.steps = []
        self.timer = QTimer()
        self.timer.timeout.connect(self.draw_next_step)
        self.step_index = 0

    def generate_graph(self):
        self.scene.clear()
        self.positions = {}
        self.step_index = 0

        n = int(self.node_input.text())
        m = int(self.edge_input.text())
        self.edges = generate_random_graph(n, m)
        self.steps = kruskal_with_steps(n, self.edges)

        if self.layout_choice.currentText() == "Daire":
            self.arrange_nodes_circle(n)
        elif self.layout_choice.currentText() == "Grid":
            self.arrange_nodes_grid(n)

        self.draw_nodes(n)
        self.info_label.setText(f"Tüm {n} düğüm başarıyla oluşturuldu. Graf: {m} kenar içeriyor.")

    def reset_scene(self):
        self.scene.clear()
        self.positions = {}
        self.steps = []
        self.step_index = 0
        self.info_label.setText("Görselleştirme sıfırlandı.")

    def arrange_nodes_circle(self, n):
        w, h = self.view.width(), self.view.height()
        r = min(w, h) // 2 - 50
        cx, cy = w // 2, h // 2
        for i in range(n):
            angle = 2 * math.pi * i / n
            x = cx + r * math.cos(angle)
            y = cy + r * math.sin(angle)
            self.positions[i] = (x, y)

    def arrange_nodes_grid(self, n):
        cols = int(math.sqrt(n)) + 1
        spacing = 40
        for i in range(n):
            row = i // cols
            col = i % cols
            x = 50 + col * spacing
            y = 50 + row * spacing
            self.positions[i] = (x, y)

    def draw_nodes(self, n):
        for i in range(n):
            x, y = self.positions[i]
            self.scene.addEllipse(x - 2, y - 2, 4, 4)

    def start_animation(self):
        self.timer.start(self.slider.value())

    def stop_animation(self):
        self.timer.stop()

    def draw_next_step(self):
        if self.step_index < len(self.steps):
            u, v, _ = self.steps[self.step_index]
            x1, y1 = self.positions[u]
            x2, y2 = self.positions[v]
            pen = QPen(QColor("blue"))
            self.scene.addLine(x1, y1, x2, y2, pen)
            self.step_index += 1
        else:
            self.timer.stop()
            self.info_label.setText(f"MST tamamlandı: {len(self.steps)} kenar")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = KruskalVisualizer()
    window.show()
    sys.exit(app.exec_())
