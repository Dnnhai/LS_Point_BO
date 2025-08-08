import random
import string
from datetime import datetime
from typing import Dict


class UserDataGenerator:
    firstname = ["Nguyễn", "Trần", "Lê", "Phạm", "Hồ", "Vũ", "Bùi", "Đặng", "Phan", "Mai", "Đoàn", "Cao", "Tôn", "Lý",
                 "Trương", "Nguyễn", "Văn", "Trần", "Thị", "Lê", "Minh", "Phạm", "Quang", "Dương"]

    middlename = ["Văn", "Thị", "Minh", "Quang", "Hoàng", "Đức", "Thái", "Hữu", "Quốc", "Tuấn", "Bảo", "Tấn", "Thanh",
                  "Mai", "Phương", "Ngọc", "Anh", "Lan", "Khánh", "Hương"]

    lastname = ["Anh", "Bình", "Cường", "Duy", "Đức", "Gia", "Hòa", "Hoàng", "Hùng", "Huy", "Khánh", "Kiên", "Khoa",
                "Lam", "Lâm", "Minh", "Nam", "Nghĩa", "Phát", "Phú", "Quang", "Quý", "Sơn", "Thành", "Thái", "Thắng",
                "Thế", "Thịnh", "Tiến", "Toàn", "Trí", "Trung", "Tuấn", "Tùng", "Vương", "Vy", "Yên", "Tâm", "Lan",
                "Lợi"]

    @staticmethod
    def generate_phone_number(prefix="09") -> str:
        return prefix + ''.join(random.choices(string.digits, k=8))

    @staticmethod
    def generate_email(domain="testing.com") -> str:
        username = ''.join(random.choices(string.ascii_lowercase, k=6))
        return f"{username}@{domain}"

    @staticmethod
    def random_combine(list1, list2, list3):
        combine_result = list(zip(
            random.sample(list1, len(list1)),
            random.sample(list2, len(list2)),
            random.sample(list3, len(list3))
        ))
        return combine_result[0]

    @staticmethod
    def generate_random_name():
        the_name = UserDataGenerator.random_combine(UserDataGenerator.firstname,
                                                    UserDataGenerator.middlename,
                                                    UserDataGenerator.lastname)
        the_name = " ".join(the_name)
        return the_name

    @staticmethod
    def generate_random_ID(length=10) -> str:
        return (''.join(random.choices(string.ascii_letters + string.digits, k=length))).upper()

    @staticmethod
    def generate_user_profile_data() -> Dict[str, str]:
        return {
            "phoneNumber": UserDataGenerator.generate_phone_number(),
            "email": UserDataGenerator.generate_email(),
            "username": UserDataGenerator.generate_random_name(),
            "userID": UserDataGenerator.generate_random_ID()
        }


# Nếu chạy file trực tiếp, in thử ra 1 bộ dữ liệu
if __name__ == "__main__":
    print(UserDataGenerator.generate_user_profile_data())

