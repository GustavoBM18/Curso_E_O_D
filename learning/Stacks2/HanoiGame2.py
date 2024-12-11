import tkinter as tk
from tkinter import messagebox
from StackHanoi import Stack
import logging

# Asegúrate de configurar el logging
logging.basicConfig(level=logging.WARNING)

class HanoiGame:
    def __init__(self, master, num_disks):
        self.master = master
        self.master.title("Torres de Hanoi")
        self.stacks = [Stack("Izquierda"), Stack("Medio"), Stack("Derecha")]
        self.num_disks = num_disks
        self.num_user_moves = 0
        self.create_widgets()
        self.initialize_game()

    def create_widgets(self):
        self.left_frame = tk.Frame(self.master)
        self.middle_frame = tk.Frame(self.master)
        self.right_frame = tk.Frame(self.master)

        self.left_frame.pack(side='left')
        self.middle_frame.pack(side='left')
        self.right_frame.pack(side='left')

        self.left_label = tk.Label(self.left_frame, text="Izquierda")
        self.middle_label = tk.Label(self.middle_frame, text="Medio")
        self.right_label = tk.Label(self.right_frame, text="Derecha")

        self.left_label.pack()
        self.middle_label.pack()
        self.right_label.pack()

        self.move_button = tk.Button(self.master, text="Mover Disco", command=self.move_disk)
        self.move_button.pack()

        self.status_label = tk.Label(self.master, text="")
        self.status_label.pack()

        self.from_stack_var = tk.StringVar(value="L")
        self.to_stack_var = tk.StringVar(value="R")
        
        self.from_stack_menu = tk.OptionMenu(self.master, self.from_stack_var, "L", "M", "R")
        self.to_stack_menu = tk.OptionMenu(self.master, self.to_stack_var, "L", "M", "R")

        self.from_stack_menu.pack()
        self.to_stack_menu.pack()

        self.optimal_moves_label = tk.Label(self.master, text="")
        self.optimal_moves_label.pack()

        self.disks_frame = tk.Frame(self.master)
        self.disks_frame.pack()

        self.disks_label = tk.Label(self.disks_frame, text="¿Con cuántos discos quieres jugar?")
        self.disks_label.pack(side='left')

        self.disks_entry = tk.Entry(self.disks_frame)
        self.disks_entry.pack(side='left')

        self.start_button = tk.Button(self.disks_frame, text="Iniciar Juego", command=self.start_game)
        self.start_button.pack(side='left')
        
    def start_game(self):
        try:
            num_disks = int(self.disks_entry.get())
            if num_disks < 3:
                messagebox.showerror("Error", "Ingresa un número mayor o igual a 3.")
            else:
                self.num_disks = num_disks
                self.stacks = [Stack("Izquierda"), Stack("Medio"), Stack("Derecha")]
                self.num_user_moves = 0
                self.initialize_game()
                self.optimal_moves = 2 ** self.num_disks - 1
                self.optimal_moves_label.config(text=f"Número óptimo de movimientos: {self.optimal_moves}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa un número válido.")

    def initialize_game(self):
        for disk in range(self.num_disks, 0, -1):
            self.stacks[0].push(disk)
        self.update_display()

    def update_display(self):
        for frame, stack in zip([self.left_frame, self.middle_frame, self.right_frame], self.stacks):
            for widget in frame.winfo_children():
                widget.destroy()
            label = tk.Label(frame, text=stack.get_name())
            label.pack()
            current_node = stack.top_item
            while current_node:
                disk_label = tk.Label(frame, text=str(current_node.get_value()), bg="gray", width=current_node.get_value())
                disk_label.pack()
                current_node = current_node.get_next_node()

    def move_disk(self):
        from_stack_index = {'L': 0, 'M': 1, 'R': 2}[self.from_stack_var.get()]
        to_stack_index = {'L': 0, 'M': 1, 'R': 2}[self.to_stack_var.get()]

        from_stack = self.stacks[from_stack_index]
        to_stack = self.stacks[to_stack_index]

        if from_stack.is_empty():
            messagebox.showerror("Error", "Movimiento no válido. La pila de origen está vacía.")
            return
        
        if to_stack.is_empty() or from_stack.peek() < to_stack.peek():
            disk = from_stack.pop()
            to_stack.push(disk)
            self.num_user_moves += 1
            self.update_display()

            if self.stacks[2].get_size() == self.num_disks:
                messagebox.showinfo("Juego Completo", f"Completaste el juego en {self.num_user_moves} movimientos")
        else:
            messagebox.showerror("Error", "Movimiento no válido. No puedes colocar un disco más grande encima de uno más pequeño.")

if __name__ == "__main__":
    root = tk.Tk()
    app = HanoiGame(root, 3)  # Inicializa con 3 discos, el valor se cambiará en la interfaz
    root.mainloop()

