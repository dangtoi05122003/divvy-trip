import zipfile
import io
from utils import get_logger

logger = get_logger(__name__)
def extract_csv(zip_content: bytes):
    with zipfile.ZipFile(io.BytesIO(zip_content)) as z:
        csv_files = [name for name in z.namelist() if name.endswith(".csv") and not name.startswith("__MACOSX")]
        if not csv_files:
            logger.error("Csv not found")
        print(csv_files)
        csv_name = csv_files[0]
        csv_content = z.read(csv_name)
        return csv_name, csv_content