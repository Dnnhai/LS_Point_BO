import os
import datetime
import logging


class Utils:
    @staticmethod
    def get_TOTP(self):
        pass

    @staticmethod
    def save_to_file(text, filename="outputs_user_register_BO.txt"):
        logging.info("Save data to file")
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, "..", f"Reports/{filename}")

        with open(file_path, "a", encoding="utf-8") as f:
            f.write(f" {text}  -  {timestamp}" "\n")
