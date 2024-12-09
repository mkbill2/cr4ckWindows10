import os
import subprocess
import webbrowser
from colorama import Fore, Style, init
import sys
import ctypes

def is_admin():
    """Kiểm tra xem chương trình có đang chạy với quyền admin không."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    # Yêu cầu chạy lại với quyền admin
    print("Đang khởi chạy lại chương trình với quyền admin...")
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit()


# Phần code chính ở đây
print("Đã chạy với quyền admin!")


# Khởi tạo colorama
init(autoreset=True)

def clear_console():
    """Xóa màn hình console."""
    os.system('cls' if os.name == 'nt' else 'clear')

def execute_command(command):
    """Thực thi lệnh hệ thống và trả về kết quả."""
    try:
        result = subprocess.run(command, check=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout.strip(), None
    except subprocess.CalledProcessError as e:
        return None, e.stderr.strip()

def open_website():
    """Mở trang web www.me.org trong trình duyệt."""
    print(Fore.YELLOW + "DONATE ME !")
    webbrowser.open("https://playerduo.net/66866365a76094c7ca3dd32e", new=2)  # new=2 mở trang web trong tab mới của trình duyệt

def remove_kms():
    """Xóa cấu hình KMS."""
    clear_console()
    print(Fore.CYAN + Style.BRIGHT + "=== Gỡ Bỏ KMS Server ===\n")

    # Xóa KMS Host
    print(Fore.YELLOW + "Bước 1: Xóa KMS Host...")
    _, error = execute_command('slmgr /ckms')
    if error:
        print(Fore.RED + f"Lỗi khi xóa KMS Host: {error}")
    else:
        print(Fore.GREEN + "KMS Host đã được xóa thành công.\n")

    # Gỡ bỏ Product Key hiện tại
    print(Fore.YELLOW + "Bước 2: Gỡ bỏ Product Key hiện tại...")
    _, error = execute_command('slmgr /upk')
    if error:
        print(Fore.RED + f"Lỗi khi gỡ Product Key: {error}")
    else:
        print(Fore.GREEN + "Product Key đã được gỡ bỏ thành công.\n")

    # Cài đặt Product Key mặc định
    print(Fore.YELLOW + "Bước 3: Cài đặt Product Key mặc định...")
    default_key = "	N9XJ7-7DBP2-PDFPG-JPMK6-QYH26"  # Key mặc định cho Windows Enterprise
    _, error = execute_command(f'slmgr /ipk {default_key}')
    if error:
        print(Fore.RED + f"Lỗi khi cài đặt Product Key mặc định: {error}")
    else:
        print(Fore.GREEN + f"Product Key mặc định đã được cài đặt: {default_key}\n")

    print(Fore.CYAN + Style.BRIGHT + "=== Đã gỡ bỏ KMS Server thành công ===")

def apply_kms_key():
    """Cài đặt và kích hoạt KMS."""
    clear_console()
    print(Fore.CYAN + Style.BRIGHT + "=== KMS Activation Script ===")

    # Nhập Product Key
    product_key = input(Fore.YELLOW + "Nhập Product Key (ví dụ: W269N-WFGWX-YVC9B-4J6C9-T83GX): ").strip()
    
    # Nhập KMS Host
    kms_host = input(Fore.YELLOW + "Nhập KMS Host (ví dụ: kms.example.com): ").strip()
    
    clear_console()
    print(Fore.BLUE + "Đang tiến hành kích hoạt Windows...\n")

    # Cài đặt Product Key
    print(Fore.GREEN + "Bước 1: Cài đặt Product Key...")
    output, error = execute_command(f'slmgr /ipk {product_key}')
    if error:
        print(Fore.RED + f"Lỗi cài đặt Product Key: {error}")
        return

    print(Fore.GREEN + "Product Key đã được cài đặt thành công.\n")

    # Thiết lập KMS Host
    print(Fore.GREEN + f"Bước 2: Thiết lập KMS Host ({kms_host})...")
    output, error = execute_command(f'slmgr /skms {kms_host}')
    if error:
        print(Fore.RED + f"Lỗi thiết lập KMS Host: {error}")
        return

    print(Fore.GREEN + f"KMS Host đã được thiết lập: {kms_host}\n")

    # Kích hoạt Windows
    print(Fore.GREEN + "Bước 3: Kích hoạt Windows...")
    output, error = execute_command('slmgr /ato')
    if error:
        if "0xC004F074" in error:
            print(Fore.RED + "Lỗi: Không thể kết nối đến KMS Server. Vui lòng kiểm tra KMS Host.")
        elif "0xC004F050" in error:
            print(Fore.RED + "Lỗi: Product Key không hợp lệ hoặc không tồn tại.")
        elif "0xC004F034" in error:
            print(Fore.RED + "Lỗi: Product Key không tương thích với phiên bản Windows.")
        else:
            print(Fore.RED + f"Lỗi kích hoạt: {error}")
        return

    print(Fore.GREEN + Style.BRIGHT + "Kích hoạt Windows thành công!\n")

def main():
    """Menu chính."""
    open_website()  # Mở trang web ngay khi chạy chương trình

    while True:
        clear_console()
        print(Fore.CYAN + Style.BRIGHT + "=== Crack Windows 10 Vip Pro Max ===")
        print("1. Kích hoạt Windows với KMS")
        print("2. Gỡ bỏ KMS Server")
        print("3. Thoát")
        print(Fore.RED + Style.BRIGHT + "TOOL CRACK WINDOWS 10 PRO BY @lunaytzzz")
        choice = input(Fore.YELLOW + "Chọn một tùy chọn (1-3): ").strip()

        if choice == "1":
            apply_kms_key()
        elif choice == "2":
            remove_kms()
        elif choice == "3":
            print(Fore.GREEN + "Đã thoát chương trình.")
            break
        else:
            print(Fore.RED + "Lựa chọn không hợp lệ. Vui lòng thử lại!")
            input("Nhấn Enter để tiếp tục...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.RED + "\nĐã hủy thao tác.")
