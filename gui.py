import customtkinter as ctk
from tkinter import messagebox
from graph_backend import Graph

# ---------------- SETTINGS ----------------
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# ---------------- GRAPH OBJECT ----------------
g = Graph()

# ---------------- WINDOW ----------------
window = ctk.CTk()
window.title("Graph Construction & Traversal")
window.geometry("1000x750")

# ⭐ WHITE BACKGROUND
window.configure(fg_color="white")

# ---------------- TITLE ----------------
title = ctk.CTkLabel(
    window,
    text="Graph Construction & Traversal ",
    font=("Arial", 26, "bold"),
    text_color="black"
)
title.pack(pady=15)

# ---------------- MAIN FRAME ----------------
frame = ctk.CTkFrame(
    window,
    fg_color="#F3F4F6"   # light grey card
)
frame.pack(padx=20, pady=10, fill="both", expand=True)

# =====================================================
# ENTRY CARD (CENTERED CLEAN LAYOUT)
# =====================================================
entry_card = ctk.CTkFrame(
    frame,
    fg_color="white",
    corner_radius=15
)
entry_card.pack(pady=20, padx=20)

# ---------------- NODE ENTRY ----------------
node_label = ctk.CTkLabel(
    entry_card,
    text="Node",
    text_color="black"
)
node_label.grid(row=0, column=0, padx=10, pady=10)

node_entry = ctk.CTkEntry(
    entry_card,
    width=200,
    placeholder_text="Enter node"
)
node_entry.grid(row=0, column=1, padx=10, pady=10)

def add_node():
    node = node_entry.get()

    if node:
        g.add_node(node)
        messagebox.showinfo("Success", f"Node {node} added")
        node_entry.delete(0, "end")
    else:
        messagebox.showerror("Error", "Enter node")

add_node_btn = ctk.CTkButton(
    entry_card,
    text="Add Node",
    command=add_node
)
add_node_btn.grid(row=0, column=2, padx=10)

# ---------------- EDGE ENTRY ----------------
u_entry = ctk.CTkEntry(entry_card, width=150, placeholder_text="Node A")
v_entry = ctk.CTkEntry(entry_card, width=150, placeholder_text="Node B")
w_entry = ctk.CTkEntry(entry_card, width=150, placeholder_text="Weight")

u_entry.grid(row=1, column=0, padx=10, pady=10)
v_entry.grid(row=1, column=1, padx=10, pady=10)
w_entry.grid(row=1, column=2, padx=10, pady=10)

def add_edge():
    u = u_entry.get()
    v = v_entry.get()
    w = w_entry.get()

    if u and v and w:
        g.add_edge(u, v, int(w))
        messagebox.showinfo("Success", f"Edge {u}-{v} added")
        u_entry.delete(0, "end")
        v_entry.delete(0, "end")
        w_entry.delete(0, "end")
    else:
        messagebox.showerror("Error", "Fill all fields")

add_edge_btn = ctk.CTkButton(
    entry_card,
    text="Add Edge",
    command=add_edge
)
add_edge_btn.grid(row=1, column=3, padx=10)

# ---------------- START / END ----------------
start_entry = ctk.CTkEntry(frame, width=250, placeholder_text="Start Node")
start_entry.pack(pady=10)

end_entry = ctk.CTkEntry(frame, width=250, placeholder_text="Destination Node")
end_entry.pack(pady=5)

# ---------------- OUTPUT BOX ----------------
output_box = ctk.CTkTextbox(
    frame,
    width=700,
    height=200,
    font=("Consolas", 14)
)
output_box.pack(pady=20)

# ---------------- BFS ----------------
def run_bfs():
    start = start_entry.get()

    if start in g.graph:
        result = g.bfs(start)
        output_box.delete("1.0", "end")
        output_box.insert("end", "BFS:\n" + " -> ".join(result))
    else:
        messagebox.showerror("Error", "Invalid node")

# ---------------- DFS ----------------
def run_dfs():
    start = start_entry.get()

    if start in g.graph:
        result = g.dfs(start)
        output_box.delete("1.0", "end")
        output_box.insert("end", "DFS:\n" + " -> ".join(result))
    else:
        messagebox.showerror("Error", "Invalid node")

# ---------------- DIJKSTRA ----------------
def run_dijkstra():
    start = start_entry.get()
    end = end_entry.get()

    if start in g.graph and end in g.graph:
        path, cost = g.dijkstra(start, end)
        output_box.delete("1.0", "end")
        output_box.insert("end", f"Shortest Path:\n{' -> '.join(path)}\nCost: {cost}")
    else:
        messagebox.showerror("Error", "Invalid nodes")

# ---------------- BUTTONS ----------------
btn_frame = ctk.CTkFrame(frame, fg_color="transparent")
btn_frame.pack(pady=10)

ctk.CTkButton(btn_frame, text="BFS", command=run_bfs).grid(row=0, column=0, padx=10)
ctk.CTkButton(btn_frame, text="DFS", command=run_dfs).grid(row=0, column=1, padx=10)
ctk.CTkButton(btn_frame, text="Dijkstra", command=run_dijkstra).grid(row=0, column=2, padx=10)

# ---------------- VISUALIZE ----------------
ctk.CTkButton(
    frame,
    text="Visualize Graph",
    fg_color="green",
    command=g.visualize
).pack(pady=10)

# ---------------- CLEAR ----------------
def clear_output():
    output_box.delete("1.0", "end")

ctk.CTkButton(
    frame,
    text="Clear Output",
    fg_color="red",
    command=clear_output
).pack(pady=5)

# ---------------- RUN ----------------
window.mainloop()