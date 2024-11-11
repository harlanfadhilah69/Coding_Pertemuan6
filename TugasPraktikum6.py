import tkinter as tk
from tkinter import messagebox


def hasil_prediksi():
    try:
        
        nilai = []
        for entry in entries:
            value = float(entry.get())
            if value < 0 or value > 100:
                raise ValueError("Nilai harus antara 0 sampai 100")
            nilai.append(value)
        
        hasil_label.config(text="Prodi Pilihan: Teknologi Informasi")
        
    except ValueError:
        messagebox.showerror("Error", "Nilai harus berupa angka antara 0 sampai 100 dan tidak boleh berupa huruf")
    


root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("500x700")
root.configure(bg = "cyan")


judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", fg ="blue", font=("Arial", 16, "bold"))
judul_label.pack(pady=10)


entry_labels = []
entries = []
for i in range(1, 11):
    label = tk.Label(root, text=f"Nilai Mata Pelajaran {i}:", fg = "darkred", font=("Arial", 10))
    label.pack(pady=5)
    entry = tk.Entry(root, width=30)
    entry.pack()
    entry_labels.append(label)
    entries.append(entry)


prediksi_button = tk.Button(root, text="Hasil Prediksi", fg = "black", command=hasil_prediksi)
prediksi_button.pack(pady=20)


hasil_label = tk.Label(root, text="Hasil Prediksi", font=("Arial", 12, "bold"))
hasil_label.pack(pady=20)



root.mainloop()