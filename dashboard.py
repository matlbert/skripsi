import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import tkinter.font as tkfont
import tkinter.scrolledtext as tkscrolled
import customtkinter
import os
from PIL import Image, ImageTk

def center_window(window, width, height):
    # Mendapatkan lebar dan tinggi layar
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Menghitung posisi x dan y untuk jendela agar berada di tengah layar
    x = int((screen_width/2) - (width/2))
    y = int((screen_height/2) - (height/2))

    # Menentukan posisi jendela
    root.geometry(f"{width}x{height}+{x}+{y}")
    root.resizable(False,False)

def center_content(frame):
    # Mengatur properti grid agar konten berada di tengah
    frame.grid_configure(padx=10, pady=10)

    # Mengatur properti grid untuk seluruh widget di dalam frame
    for widget in frame.winfo_children():
        widget.grid_configure(padx=5, pady=5)
        
def show_dashboard():
    # Hapus konten sebelumnya (jika ada)
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Tambahkan konten dashboard
    dashboard_label = customtkinter.CTkLabel(content_frame, text="Halaman Dashboard")
    dashboard_label.pack()

def show_pembelian():
# Hapus konten sebelumnya (jika ada)
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Tambahkan konten pembelian
    pembelian_label = customtkinter.CTkLabel(content_frame, text="Halaman Pembelian", font=("Arial",30))
    pembelian_label.grid(row=0, column=1, padx=0, pady=20, columnspan=2)

    # Field Tanggal Pembelian
    tanggal_label = customtkinter.CTkLabel(content_frame, text="Tanggal Pembelian:", font=("Arial",16))
    tanggal_label.grid(row=1, column=0, padx=20, pady=10)
    tanggal_entry = customtkinter.CTkEntry(content_frame, width=200)
    tanggal_entry.grid(row=1, column=1)

    # Field ID Pembelian
    id_label = customtkinter.CTkLabel(content_frame, text="ID Pembelian:", font=("Arial",16))
    id_label.grid(row=2, column=0, padx=20, pady=10)
    id_entry = customtkinter.CTkEntry(content_frame, width=200)
    id_entry.grid(row=2, column=1)

    # Field ID Supplier
    supplier_label = customtkinter.CTkLabel(content_frame, text="ID Supplier:", font=("Arial",16))
    supplier_label.grid(row=3, column=0, padx=20, pady=10)
    supplier_entry = customtkinter.CTkEntry(content_frame, width=200)
    supplier_entry.grid(row=3, column=1)

    # Field ID Bahan Baku
    bahanbaku_label = customtkinter.CTkLabel(content_frame, text="ID Bahan Baku:", font=("Arial",16))
    bahanbaku_label.grid(row=4, column=0, padx=20, pady=10)
    bahanbaku_entry = customtkinter.CTkEntry(content_frame, width=200)
    bahanbaku_entry.grid(row=4, column=1)

    # Field Jumlah
    jumlah_label = customtkinter.CTkLabel(content_frame, text="Jumlah:", font=("Arial",16))
    jumlah_label.grid(row=5, column=0, padx=20, pady=10)
    jumlah_entry = customtkinter.CTkEntry(content_frame, width=200)
    jumlah_entry.grid(row=5, column=1)

    # Field Total Harga
    totalharga_label = customtkinter.CTkLabel(content_frame, text="Total Harga:", font=("Arial",16))
    totalharga_label.grid(row=6, column=0, padx=20, pady=10)
    totalharga_entry = customtkinter.CTkEntry(content_frame, width=200)
    totalharga_entry.grid(row=6, column=1)

    # Field Total Pembayaran
    totalpembayaran_label = customtkinter.CTkLabel(content_frame, text="Total Pembayaran:", font=("Arial",16))
    totalpembayaran_label.grid(row=7, column=0, padx=20, pady=10)
    totalpembayaran_entry = customtkinter.CTkEntry(content_frame, width=200)
    totalpembayaran_entry.grid(row=7, column=1)

    # Field Sisa Pembayaran
    sisapembayaran_label = customtkinter.CTkLabel(content_frame, text="Sisa Pembayaran:", font=("Arial",16))
    sisapembayaran_label.grid(row=8, column=0, padx=20, pady=10, width=200)
    sisapembayaran_entry = customtkinter.CTkEntry(content_frame)
    sisapembayaran_entry.grid(row=8, column=1)

    # Tombol Simpan
    simpan_button = customtkinter.CTkButton(content_frame, text="Simpan", command=lambda: simpan_pembelian(tanggal_entry.get(), id_entry.get(), supplier_entry.get(), bahanbaku_entry.get(), jumlah_entry.get(), totalharga_entry.get(), totalpembayaran_entry.get(), sisapembayaran_entry.get()))
    simpan_button.grid(row=9, column=0, columnspan=2, pady=10)

def show_datapembelian():
    # Hapus konten sebelumnya (jika ada)
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Tambahkan konten pembelian
    datapembelian_label = customtkinter.CTkLabel(content_frame, text="Data Pembelian")
    datapembelian_label.pack(pady=12)

def show_penjualan():
    # Hapus konten sebelumnya (jika ada)
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Tambahkan konten penjualan
    penjualan_label = customtkinter.CTkLabel(content_frame, text="Halaman Penjualan")
    penjualan_label.grid(row=0, column=0, columnspan=2, pady=10)

    # Field Tanggal Penjualan
    tanggal_label = customtkinter.CTkLabel(content_frame, text="Tanggal Penjualan:")
    tanggal_label.grid(row=1, column=0, sticky="e")
    tanggal_entry = customtkinter.CTkEntry(content_frame)
    tanggal_entry.grid(row=1, column=1)

    # Field ID Penjualan
    id_label = customtkinter.CTkLabel(content_frame, text="ID Penjualan:")
    id_label.grid(row=2, column=0, sticky="e")
    id_entry = customtkinter.CTkEntry(content_frame)
    id_entry.grid(row=2, column=1)

    # Field ID Produk
    produk_label = customtkinter.CTkLabel(content_frame, text="ID Produk:")
    produk_label.grid(row=3, column=0, sticky="e")
    produk_entry = customtkinter.CTkEntry(content_frame)
    produk_entry.grid(row=3, column=1)

    # Field Nama Produk
    namaproduk_label = customtkinter.CTkLabel(content_frame, text="Nama Produk:")
    namaproduk_label.grid(row=4, column=0, sticky="e")
    namaproduk_entry = customtkinter.CTkEntry(content_frame)
    namaproduk_entry.grid(row=4, column=1)

    # Field Jumlah
    jumlah_label = customtkinter.CTkLabel(content_frame, text="Jumlah:")
    jumlah_label.grid(row=5, column=0, sticky="e")
    jumlah_entry = customtkinter.CTkEntry(content_frame)
    jumlah_entry.grid(row=5, column=1)

    # Field Total Harga
    totalharga_label = customtkinter.CTkLabel(content_frame, text="Total Harga:")
    totalharga_label.grid(row=6, column=0, sticky="e")
    totalharga_entry = customtkinter.CTkEntry(content_frame)
    totalharga_entry.grid(row=6, column=1)

    # Field Harga Jual
    hargajual_label = customtkinter.CTkLabel(content_frame, text="Harga Jual:")
    hargajual_label.grid(row=7, column=0, sticky="e")
    hargajual_entry = customtkinter.CTkEntry(content_frame)
    hargajual_entry.grid(row=7, column=1)

    # Field Total Pembayaran
    totalpembayaran_label = customtkinter.CTkLabel(content_frame, text="Total Pembayaran:")
    totalpembayaran_label.grid(row=8, column=0, sticky="e")
    totalpembayaran_entry = customtkinter.CTkEntry(content_frame)
    totalpembayaran_entry.grid(row=8, column=1)

    # Field Sisa Pembayaran (Piutang)
    sisapembayaran_label = customtkinter.CTkLabel(content_frame, text="Sisa Pembayaran (Piutang):")
    sisapembayaran_label.grid(row=9, column=0, sticky="e")
    sisapembayaran_entry = customtkinter.CTkEntry(content_frame)
    sisapembayaran_entry.grid(row=9, column=1)

    # Tombol Simpan
    simpan_button = customtkinter.CTkButton(content_frame, text="Simpan", command=lambda: simpan_penjualan(tanggal_entry.get(), id_entry.get(), produk_entry.get(), namaproduk_entry.get(), jumlah_entry.get(), totalharga_entry.get(), hargajual_entry.get(), totalpembayaran_entry.get(), sisapembayaran_entry.get()))
    simpan_button.grid(row=10, column=0, columnspan=2, pady=10)

def show_datapenjualan():
    # Hapus konten sebelumnya (jika ada)
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Tambahkan konten penjualan
    datapenjualan_label = customtkinter.CTkLabel(content_frame, text="Data Penjualan")
    datapenjualan_label.grid(row=0, column=0, columnspan=2, pady=10)

def show_produksi():
    # Hapus konten sebelumnya (jika ada)
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Tambahkan konten produksi
    produksi_label = customtkinter.CTkLabel(content_frame, text="Halaman Produksi")
    produksi_label.grid(row=0, column=0, columnspan=2, pady=10)

    # Field Tanggal Produksi
    tanggal_label = customtkinter.CTkLabel(content_frame, text="Tanggal Produksi:")
    tanggal_label.grid(row=1, column=0, sticky="e")
    tanggal_entry = customtkinter.CTkEntry(content_frame)
    tanggal_entry.grid(row=1, column=1)

    # Field ID Produksi
    id_label = customtkinter.CTkLabel(content_frame, text="ID Produksi:")
    id_label.grid(row=2, column=0, sticky="e")
    id_entry = customtkinter.CTkEntry(content_frame)
    id_entry.grid(row=2, column=1)

    # Field ID Bahan Baku
    idbahanbaku_label = customtkinter.CTkLabel(content_frame, text="ID Bahan Baku:")
    idbahanbaku_label.grid(row=3, column=0, sticky="e")
    idbahanbaku_entry = customtkinter.CTkEntry(content_frame)
    idbahanbaku_entry.grid(row=3, column=1)

    # Field Nama Bahan Baku
    namabahanbaku_label = customtkinter.CTkLabel(content_frame, text="Nama Bahan Baku:")
    namabahanbaku_label.grid(row=4, column=0, sticky="e")
    namabahanbaku_entry = customtkinter.CTkEntry(content_frame)
    namabahanbaku_entry.grid(row=4, column=1)

    # Field Jumlah Bahan Baku
    jumlahbahanbaku_label = customtkinter.CTkLabel(content_frame, text="Jumlah Bahan Baku:")
    jumlahbahanbaku_label.grid(row=5, column=0, sticky="e")
    jumlahbahanbaku_entry = customtkinter.CTkEntry(content_frame)
    jumlahbahanbaku_entry.grid(row=5, column=1)

    # Field Harga Bahan Baku
    hargabahanbaku_label = customtkinter.CTkLabel(content_frame, text="Harga Bahan Baku:")
    hargabahanbaku_label.grid(row=6, column=0, sticky="e")
    hargabahanbaku_entry = customtkinter.CTkEntry(content_frame)
    hargabahanbaku_entry.grid(row=6, column=1)

    # Field Total Biaya Bahan Baku
    totalbiayabahanbaku_label = customtkinter.CTkLabel(content_frame, text="Total Biaya Bahan Baku:")
    totalbiayabahanbaku_label.grid(row=7, column=0, sticky="e")
    totalbiayabahanbaku_entry = customtkinter.CTkEntry(content_frame)
    totalbiayabahanbaku_entry.grid(row=7, column=1)

    # Field ID Produk
    idproduk_label = customtkinter.CTkLabel(content_frame, text="ID Produk:")
    idproduk_label.grid(row=8, column=0, sticky="e")
    idproduk_entry = customtkinter.CTkEntry(content_frame)
    idproduk_entry.grid(row=8, column=1)

    # Field Output Produksi
    outputproduksi_label = customtkinter.CTkLabel(content_frame, text="Output Produksi:")
    outputproduksi_label.grid(row=9, column=0, sticky="e")
    outputproduksi_entry = customtkinter.CTkEntry(content_frame)
    outputproduksi_entry.grid(row=9, column=1)

    # Tombol Simpan
    simpan_button = customtkinter.CTkButton(content_frame, text="Simpan", command=lambda: simpan_produksi(tanggal_entry.get(), id_entry.get(), idbahanbaku_entry.get(), namabahanbaku_entry.get(), jumlahbahanbaku_entry.get(), hargabahanbaku_entry.get(), totalbiayabahanbaku_entry.get(), idproduk_entry.get(), outputproduksi_entry.get()))
    simpan_button.grid(row=10, column=0, columnspan=2, pady=10)

def show_dataproduksi():
    # Hapus konten sebelumnya (jika ada)
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Tambahkan konten produksi
    dataproduksi_label = customtkinter.CTkLabel(content_frame, text="Data Produksi")
    dataproduksi_label.grid(row=0, column=0, columnspan=2, pady=10)

def show_penerimaan():
    # Hapus konten sebelumnya (jika ada)
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Tambahkan konten penerimaan
    penerimaan_label = customtkinter.CTkLabel(content_frame, text="Halaman Penerimaan")
    penerimaan_label.grid(row=0, column=0, columnspan=2, pady=10)

    # Field Tanggal Penerimaan
    tanggal_label = customtkinter.CTkLabel(content_frame, text="Tanggal Penerimaan:")
    tanggal_label.grid(row=1, column=0, sticky="e")
    tanggal_entry = customtkinter.CTkEntry(content_frame)
    tanggal_entry.grid(row=1, column=1)

    # Field ID Penerimaan
    id_label = customtkinter.CTkLabel(content_frame, text="ID Penerimaan:")
    id_label.grid(row=2, column=0, sticky="e")
    id_entry = customtkinter.CTkEntry(content_frame)
    id_entry.grid(row=2, column=1)

    # Field Jenis Penerimaan
    jenis_label = customtkinter.CTkLabel(content_frame, text="Jenis Penerimaan:")
    jenis_label.grid(row=3, column=0, sticky="e")
    jenis_entry = customtkinter.CTkEntry(content_frame)
    jenis_entry.grid(row=3, column=1)

    # Field Keterangan
    keterangan_label = customtkinter.CTkLabel(content_frame, text="Keterangan:")
    keterangan_label.grid(row=4, column=0, sticky="e")
    keterangan_entry = customtkinter.CTkEntry(content_frame)
    keterangan_entry.grid(row=4, column=1)

    # Field Jumlah
    jumlah_label = customtkinter.CTkLabel(content_frame, text="Jumlah:")
    jumlah_label.grid(row=5, column=0, sticky="e")
    jumlah_entry = customtkinter.CTkEntry(content_frame)
    jumlah_entry.grid(row=5, column=1)

    # Tombol Simpan
    simpan_button = customtkinter.CTkButton(content_frame, text="Simpan", command=lambda: simpan_penerimaan(tanggal_entry.get(), id_entry.get(), jenis_entry.get(), keterangan_entry.get(), jumlah_entry.get()))
    simpan_button.grid(row=6, column=0, columnspan=2, pady=10)

def show_datapenerimaan():
    # Hapus konten sebelumnya (jika ada)
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Tambahkan konten penerimaan
    datapenerimaan_label = customtkinter.CTkLabel(content_frame, text="Data Penerimaan")
    datapenerimaan_label.grid(row=0, column=0, columnspan=2, pady=10)

def show_pengeluaran():
    # Hapus konten sebelumnya (jika ada)
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Tambahkan konten pengeluaran
    pengeluaran_label = customtkinter.CTkLabel(content_frame, text="Halaman Pengeluaran")
    pengeluaran_label.grid(row=0, column=0, columnspan=2, pady=10)

    # Field Tanggal Pengeluaran
    tanggal_label = customtkinter.CTkLabel(content_frame, text="Tanggal Pengeluaran:")
    tanggal_label.grid(row=1, column=0, sticky="e")
    tanggal_entry = customtkinter.CTkEntry(content_frame)
    tanggal_entry.grid(row=1, column=1)

    # Field ID Pengeluaran
    id_label = customtkinter.CTkLabel(content_frame, text="ID Pengeluaran:")
    id_label.grid(row=2, column=0, sticky="e")
    id_entry = customtkinter.CTkEntry(content_frame)
    id_entry.grid(row=2, column=1)

    # Field Jenis Pengeluaran
    jenis_label = customtkinter.CTkLabel(content_frame, text="Jenis Pengeluaran:")
    jenis_label.grid(row=3, column=0, sticky="e")
    jenis_entry = customtkinter.CTkEntry(content_frame)
    jenis_entry.grid(row=3, column=1)

    # Field Keterangan
    keterangan_label = customtkinter.CTkLabel(content_frame, text="Keterangan:")
    keterangan_label.grid(row=4, column=0, sticky="e")
    keterangan_entry = customtkinter.CTkEntry(content_frame)
    keterangan_entry.grid(row=4, column=1)

    # Field Jumlah
    jumlah_label = customtkinter.CTkLabel(content_frame, text="Jumlah:")
    jumlah_label.grid(row=5, column=0, sticky="e")
    jumlah_entry = customtkinter.CTkEntry(content_frame)
    jumlah_entry.grid(row=5, column=1)

    # Tombol Simpan
    simpan_button = customtkinter.CTkButton(content_frame, text="Simpan", command=lambda: simpan_pengeluaran(tanggal_entry.get(), id_entry.get(), jenis_entry.get(), keterangan_entry.get(), jumlah_entry.get()))
    simpan_button.grid(row=6, column=0, columnspan=2, pady=10)

def show_datapengeluaran():
    # Hapus konten sebelumnya (jika ada)
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Tambahkan konten pengeluaran
    datapengeluaran_label = customtkinter.CTkLabel(content_frame, text="Data Pengeluaran")
    datapengeluaran_label.grid(row=0, column=0, columnspan=2, pady=10)

def show_piutang():
    # Hapus konten sebelumnya (jika ada)
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Tambahkan konten piutang
    piutang_label = customtkinter.CTkLabel(content_frame, text="Halaman Piutang")
    piutang_label.grid(row=0, column=1, columnspan=2, pady=10)

    # Field Tanggal Piutang
    tanggal_label = customtkinter.CTkLabel(content_frame, text="Tanggal Piutang:")
    tanggal_label.grid(row=1, column=1)
    tanggal_entry = customtkinter.CTkEntry(content_frame)
    tanggal_entry.grid(row=1, column=2)

    # Field ID Piutang
    id_label = customtkinter.CTkLabel(content_frame, text="ID Piutang:")
    id_label.grid(row=2, column=1, sticky="e")
    id_entry = customtkinter.CTkEntry(content_frame)
    id_entry.grid(row=2, column=2)

    # Field ID Penjualan
    penjualan_label = customtkinter.CTkLabel(content_frame, text="ID Penjualan:")
    penjualan_label.grid(row=3, column=1, sticky="e")
    penjualan_entry = customtkinter.CTkEntry(content_frame)
    penjualan_entry.grid(row=3, column=2)

    # Field Total Piutang
    total_piutang_label = customtkinter.CTkLabel(content_frame, text="Total Piutang:")
    total_piutang_label.grid(row=4, column=1, sticky="e")
    total_piutang_entry = customtkinter.CTkEntry(content_frame)
    total_piutang_entry.grid(row=4, column=2)

    # Field Pembayaran
    pembayaran_label = customtkinter.CTkLabel(content_frame, text="Pembayaran:")
    pembayaran_label.grid(row=5, column=1, sticky="e")
    pembayaran_entry = customtkinter.CTkEntry(content_frame)
    pembayaran_entry.grid(row=5, column=2)

    # Tombol Simpan
    simpan_button = customtkinter.CTkButton(content_frame, text="Simpan", command=lambda: simpan_piutang(tanggal_entry.get(), id_entry.get(), penjualan_entry.get(), total_piutang_entry.get(), pembayaran_entry.get()))
    simpan_button.grid(row=6, column=2, columnspan=2, pady=10)

def show_datapiutang():
    # Hapus konten sebelumnya (jika ada)
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Tambahkan konten piutang
    datapiutang_label = customtkinter.CTkLabel(content_frame, text="Data Piutang")
    datapiutang_label.pack()

def show_utang():
    # Hapus konten sebelumnya (jika ada)
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Tambahkan konten utang
    utang_label = customtkinter.CTkLabel(content_frame, text="Halaman Utang")
    utang_label.grid(row=0, column=0, columnspan=2, pady=10)

    # Field Tanggal Utang
    tanggal_label = customtkinter.CTkLabel(content_frame, text="Tanggal Utang:")
    tanggal_label.grid(row=1, column=0, sticky="e")
    tanggal_entry = customtkinter.CTkEntry(content_frame)
    tanggal_entry.grid(row=1, column=1)

    # Field ID Utang
    id_label = customtkinter.CTkLabel(content_frame, text="ID Utang:")
    id_label.grid(row=2, column=0, sticky="e")
    id_entry = customtkinter.CTkEntry(content_frame)
    id_entry.grid(row=2, column=1)

    # Field ID Pembelian
    pembelian_label = customtkinter.CTkLabel(content_frame, text="ID Pembelian:")
    pembelian_label.grid(row=3, column=0, sticky="e")
    pembelian_entry = customtkinter.CTkEntry(content_frame)
    pembelian_entry.grid(row=3, column=1)

    # Field Total Utang
    total_utang_label = customtkinter.CTkLabel(content_frame, text="Total Utang:")
    total_utang_label.grid(row=4, column=0, sticky="e")
    total_utang_entry = customtkinter.CTkEntry(content_frame)
    total_utang_entry.grid(row=4, column=1)

    # Field Pembayaran
    pembayaran_label = customtkinter.CTkLabel(content_frame, text="Pembayaran:")
    pembayaran_label.grid(row=5, column=0, sticky="e")
    pembayaran_entry = customtkinter.CTkEntry(content_frame)
    pembayaran_entry.grid(row=5, column=1)

    # Tombol Simpan
    simpan_button = customtkinter.CTkButton(content_frame, text="Simpan", command=lambda: simpan_utang(tanggal_entry.get(), id_entry.get(), pembelian_entry.get(), total_utang_entry.get(), pembayaran_entry.get()))
    simpan_button.grid(row=6, column=0, columnspan=2, pady=10)

def show_datautang():
     # Hapus konten sebelumnya (jika ada)
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Tambahkan konten Utang
    datautang_label = customtkinter.CTkLabel(content_frame, text="Data Utang")
    datautang_label.grid(row=0, column=0, columnspan=2, pady=10)

def show_bahanbaku():
    # Hapus konten sebelumnya (jika ada)
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Tambahkan konten bahan baku
    bahanbaku_label = customtkinter.CTkLabel(content_frame, text="Halaman Bahan Baku")
    bahanbaku_label.grid(row=0, column=0, columnspan=2, pady=10)

    # Field ID Bahan Baku
    id_label = customtkinter.CTkLabel(content_frame, text="ID Bahan Baku:")
    id_label.grid(row=1, column=0, sticky="e")
    id_entry = customtkinter.CTkEntry(content_frame)
    id_entry.grid(row=1, column=1)

    # Field Nama Bahan Baku
    nama_label = customtkinter.CTkLabel(content_frame, text="Nama Bahan Baku:")
    nama_label.grid(row=2, column=0, sticky="e")
    nama_entry = customtkinter.CTkEntry(content_frame)
    nama_entry.grid(row=2, column=1)

    # Field Satuan
    satuan_label = customtkinter.CTkLabel(content_frame, text="Satuan:")
    satuan_label.grid(row=3, column=0, sticky="e")
    satuan_entry = customtkinter.CTkEntry(content_frame)
    satuan_entry.grid(row=3, column=1)

    # Tombol Simpan
    simpan_button = customtkinter.CTkButton(content_frame, text="Simpan", command=lambda: simpan_bahanbaku(id_entry.get(), nama_entry.get(), satuan_entry.get()))
    simpan_button.grid(row=4, column=0, columnspan=2, pady=10)

def show_produk():
    # Hapus konten sebelumnya (jika ada)
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Tambahkan konten produk
    produk_label = customtkinter.CTkLabel(content_frame, text="Halaman Produk")
    produk_label.grid(row=0, column=0, columnspan=2, pady=10)

    # Field ID Produk
    id_label = customtkinter.CTkLabel(content_frame, text="ID Produk:")
    id_label.grid(row=1, column=0, sticky="e")
    id_entry = customtkinter.CTkEntry(content_frame)
    id_entry.grid(row=1, column=1)

    # Field Nama Produk
    nama_label = customtkinter.CTkLabel(content_frame, text="Nama Produk:")
    nama_label.grid(row=2, column=0, sticky="e")
    nama_entry = customtkinter.CTkEntry(content_frame)
    nama_entry.grid(row=2, column=1)

    # Field Satuan
    satuan_label = customtkinter.CTkLabel(content_frame, text="Satuan:")
    satuan_label.grid(row=3, column=0, sticky="e")
    satuan_entry = customtkinter.CTkEntry(content_frame)
    satuan_entry.grid(row=3, column=1)

    # Tombol Simpan Produk
    simpan_button = customtkinter.CTkButton(content_frame, text="Simpan Produk", command=lambda: simpan_produk(id_entry.get(), nama_entry.get(), satuan_entry.get()))
    simpan_button.grid(row=4, column=0, columnspan=2, pady=10)

def show_supplier():
    # Hapus konten sebelumnya (jika ada)
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Tambahkan konten supplier
    supplier_label = customtkinter.CTkLabel(content_frame, text="Halaman Supplier")
    supplier_label.grid(row=0, column=0, columnspan=2, pady=10)

    # Field ID Supplier
    id_label = customtkinter.CTkLabel(content_frame, text="ID Supplier:")
    id_label.grid(row=1, column=0, sticky="e")
    id_entry = customtkinter.CTkEntry(content_frame)
    id_entry.grid(row=1, column=1)

    # Field Nama Supplier
    nama_label = customtkinter.CTkLabel(content_frame, text="Nama Supplier:")
    nama_label.grid(row=2, column=0, sticky="e")
    nama_entry = customtkinter.CTkEntry(content_frame)
    nama_entry.grid(row=2, column=1)

    # Field Alamat
    alamat_label = customtkinter.CTkLabel(content_frame, text="Alamat:")
    alamat_label.grid(row=3, column=0, sticky="e")
    alamat_entry = customtkinter.CTkEntry(content_frame)
    alamat_entry.grid(row=3, column=1)

    # Tombol Simpan Supplier
    simpan_button = customtkinter.CTkButton(content_frame, text="Simpan Supplier", command=lambda: simpan_supplier(id_entry.get(), nama_entry.get(), alamat_entry.get()))
    simpan_button.grid(row=4, column=0, columnspan=2, pady=10)

def show_pengaturan():
    # Hapus konten sebelumnya (jika ada)
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Tambahkan tombol Bahan Baku
    bahanbaku_button = customtkinter.CTkButton(content_frame, text="Bahan Baku", command=show_bahanbaku, font=("Arial",26), height=50, width=200)
    bahanbaku_button.pack(pady=120, padx=20)

    # Tambahkan tombol Produk
    produk_button = customtkinter.CTkButton(content_frame, text="Produk", command=show_produk, font=("Arial",26), height=50, width=200)
    produk_button.pack(pady=0, padx=20)

    # Tambahkan tombol Supplier
    supplier_button = customtkinter.CTkButton(content_frame, text="Supplier", command=show_supplier, font=("Arial",26), height=50, width=200)
    supplier_button.pack(pady=120, padx=20)

def show_laporan():
    # Hapus konten sebelumnya (jika ada)
    for widget in content_frame.winfo_children():
        widget.destroy()

    # # Tambahkan tombol Laporan Arus Kas
    # arus_kas_button = customtkinter.CTkButton(content_frame, text="Laporan Arus Kas", command=generate_laporan_arus_kas)
    # arus_kas_button.grid(row=0, column=0, padx=10, pady=10)

    # # Tambahkan tombol Laporan Neraca
    # neraca_button = customtkinter.CTkButton(content_frame, text="Laporan Neraca", command=generate_laporan_neraca)
    # neraca_button.grid(row=0, column=1, padx=10, pady=10)

    # # Tambahkan tombol Laporan Laba Rugi
    # laba_rugi_button = customtkinter.CTkButton(content_frame, text="Laporan Laba Rugi", command=generate_laporan_laba_rugi)
    # laba_rugi_button.grid(row=0, column=2, padx=10, pady=10)

def simpan_supplier(id_supplier, nama_supplier, alamat):
    # Lakukan operasi simpan supplier di sini
    messagebox.showinfo("Simpan Supplier", "Data Supplier berhasil disimpan.")

def simpan_produk(id_produk, nama_produk, satuan):
        # Lakukan operasi simpan supplier di sini
    messagebox.showinfo("Simpan Produk", "Data Produk berhasil disimpan.")

def simpan_bahanbaku(id_bahanbaku, nama_bahanbaku, satuan):
    # Lakukan operasi simpan bahan baku di sini
    messagebox.showinfo("Simpan Bahan Baku", "Data Bahan Baku berhasil disimpan.")

def simpan_utang(tanggal, id_utang, id_pembelian, total_utang, pembayaran):
    # Lakukan operasi simpan utang di sini
    messagebox.showinfo("Simpan Utang", "Data Utang berhasil disimpan.")

def simpan_piutang(tanggal, id_piutang, id_penjualan, total_piutang, pembayaran):
    # Lakukan operasi simpan piutang di sini
    messagebox.showinfo("Simpan Piutang", "Data Piutang berhasil disimpan.")

def simpan_pengeluaran(tanggal, id_pengeluaran, jenis_pengeluaran, keterangan, jumlah):
    # Lakukan operasi simpan pengeluaran di sini
    messagebox.showinfo("Simpan Pengeluaran", "Data Pengeluaran berhasil disimpan.")

def simpan_penerimaan(tanggal, id_penerimaan, jenis_penerimaan, keterangan, jumlah):
    # Lakukan operasi simpan penerimaan di sini
    messagebox.showinfo("Simpan Penerimaan", "Data Penerimaan berhasil disimpan.")

def simpan_produksi(tanggal, id_produksi, id_bahan_baku, nama_bahan_baku, jumlah_bahan_baku, harga_bahan_baku, total_biaya_bahan_baku, id_produk, output_produksi):
    # Lakukan operasi simpan produksi di sini
    messagebox.showinfo("Simpan Produksi", "Data Produksi berhasil disimpan.")

def simpan_pembelian(tanggal, id_pembelian, id_supplier, id_bahan_baku, jumlah, total_harga, total_pembayaran, sisa_pembayaran):
    # Lakukan operasi simpan pembelian di sini
    messagebox.showinfo("Simpan Pembelian", "Data Pembelian berhasil disimpan.")

def simpan_penjualan(tanggal, id_penjualan, id_produk, nama_produk, jumlah, total_harga, harga_jual, total_pembayaran, sisa_pembayaran):
    # Lakukan operasi simpan penjualan di sini
    messagebox.showinfo("Simpan Penjualan", "Data Penjualan berhasil disimpan.")


# Buat jendela utama
# root = tk.Tk()
# root.iconbitmap('D:/This PC/Documents/Test Code/Logo.ico')
# root.title("Sistem Informasi POS UMKM Sambal Bu Sandra")
# root.configure(background='green')

root = customtkinter.CTk(fg_color="#FF8C52")
root.iconbitmap('D:/This PC/Documents/Test Code/Logo.ico')
root.title("UMKM Sambal Bu Sandra POS")

# Mendapatkan lebar dan tinggi jendela
root_width = 800
root_height = 685

# Mengatur jendela agar berada di tengah layar
center_window(root, root_width, root_height)

# Buat frame untuk menu navigasi
menu_frame = tk.Frame(root)
menu_frame.pack(side="left", fill="y")

# load logo
file_path = os.path.dirname(os.path.realpath(__file__))
image_dashboard = customtkinter.CTkImage(Image.open(file_path + "/Logotype.png"), size=(120,55))
# menu_frame = customtkinter.CTkFrame(master=root, corner_radius=20)
# menu_frame.pack(side="left", fill="y")

# Mengatur gaya dan desain kustom
# style = ttk.Style()
# style.configure('TButton', background='red', foreground='green', font=('Arial', 10, 'bold'))

# Tombol Dashboard
dashboard_button = customtkinter.CTkButton(menu_frame, text="", image=image_dashboard, command=show_dashboard,  fg_color="#FEF4DF", hover_color="#e5dcc9")
dashboard_button.pack(padx=5, pady=5)

# Tombol Pembelian
pembelian_button = customtkinter.CTkButton(menu_frame, text="Pembelian", command=show_pembelian, fg_color="#FF8C52", hover_color="#72C822")
pembelian_button.pack(padx=5, pady=5)

# Tombol Data Pembelian
datapembelian_button = customtkinter.CTkButton(menu_frame, text="Data Pembelian", command=show_datapembelian, fg_color="#FF8C52", hover_color="#72C822")
datapembelian_button.pack(padx=5, pady=5)

# Tombol Penjualan
penjualan_button = customtkinter.CTkButton(menu_frame, text="Penjualan", command=show_penjualan, fg_color="#FF8C52", hover_color="#72C822")
penjualan_button.pack(padx=5, pady=5)

# Tombol Data Penjualan
datapenjualan_button = customtkinter.CTkButton(menu_frame, text="Data Penjualan", command=show_datapenjualan, fg_color="#FF8C52", hover_color="#72C822")
datapenjualan_button.pack(padx=5, pady=5)

# Tombol Produksi
produksi_button = customtkinter.CTkButton(menu_frame, text="Produksi", command=show_produksi, fg_color="#FF8C52", hover_color="#72C822")
produksi_button.pack(padx=5, pady=5)

# Tombol Data Produksi
dataproduksi_button = customtkinter.CTkButton(menu_frame, text="Data Produksi", command=show_dataproduksi, fg_color="#FF8C52", hover_color="#72C822")
dataproduksi_button.pack(padx=5, pady=5)

# Tombol Penerimaan
penerimaan_button = customtkinter.CTkButton(menu_frame, text="Penerimaan", command=show_penerimaan, fg_color="#FF8C52", hover_color="#72C822")
penerimaan_button.pack(padx=5, pady=5)

# Tombol Data Penerimaan
datapenerimaan_button = customtkinter.CTkButton(menu_frame, text="Data Penerimaan", command=show_datapenerimaan, fg_color="#FF8C52", hover_color="#72C822")
datapenerimaan_button.pack(padx=5, pady=5)

# Tombol Pengeluaran
pengeluaran_button = customtkinter.CTkButton(menu_frame, text="Pengeluaran", command=show_pengeluaran, fg_color="#FF8C52", hover_color="#72C822")
pengeluaran_button.pack(padx=5, pady=5)

# Tombol Data Pengeluaran
datapengeluaran_button = customtkinter.CTkButton(menu_frame, text="Data Pengeluaran", command=show_datapengeluaran, fg_color="#FF8C52", hover_color="#72C822")
datapengeluaran_button.pack(padx=5, pady=5)

# Tombol Piutang
piutang_button = customtkinter.CTkButton(menu_frame, text="Piutang", command=show_piutang, fg_color="#FF8C52", hover_color="#72C822")
piutang_button.pack(padx=5, pady=5)

# Tombol Data Piutang
datapiutang_button = customtkinter.CTkButton(menu_frame, text="Data Piutang", command=show_datapiutang, fg_color="#FF8C52", hover_color="#72C822")
datapiutang_button.pack(padx=5, pady=5)

# Tombol Utang
utang_button = customtkinter.CTkButton(menu_frame, text="Utang", command=show_utang, fg_color="#FF8C52", hover_color="#72C822")
utang_button.pack(padx=5, pady=5)

# Tombol Data Utang
datautang_button = customtkinter.CTkButton(menu_frame, text="Data Utang", command=show_datautang, fg_color="#FF8C52", hover_color="#72C822")
datautang_button.pack(padx=5, pady=5)

# Tombol Pengaturan
pengaturan_button = customtkinter.CTkButton(menu_frame, text="Pengaturan", command=show_pengaturan, fg_color="#FF8C52", hover_color="#72C822")
pengaturan_button.pack(padx=5, pady=5)

# Tombol Laporan
pengaturan_button = customtkinter.CTkButton(menu_frame, text="Laporan", command=show_laporan, fg_color="#FF8C52", hover_color="#72C822")
pengaturan_button.pack(padx=5, pady=5)

# Buat frame untuk konten
content_frame = customtkinter.CTkFrame(master=root, corner_radius=20, fg_color="#FEF4DF")
content_frame.pack(padx=10, pady=10, fill="both", expand=True)


# Tampilkan konten dashboard awal
show_dashboard()
# Jalankan aplikasi
root.mainloop()