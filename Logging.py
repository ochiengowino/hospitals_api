from datetime import datetime
import os

class Logging:
    
    @staticmethod
    def write_log(error_message):
        try:
            log_path = r"Geoportal_logs"
            if not os.path.exists(log_path):
                os.makedirs(log_path)
            
            log_file_name = os.path.join(log_path, f"{datetime.now():%Y-%b-%d}.txt")
            
            with open(log_file_name, "a") as log_file:
                log_file.write(f"{datetime.now():%Y-%b-%d %H:%M:%S}: => {error_message}\n")
        except Exception as ex:
            pass  # Optionally, handle exceptions (e.g., print(ex) or log to another location)