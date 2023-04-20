from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from predict import preprocess_image
from PIL import Image

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

bear_files = {
    "black": "Bear Facts/BlackFacts.txt",
    "grizzly": "Bear Facts/GrizzlyFacts.txt",
    "polar": "Bear Facts/PolarFacts.txt",
    "panda": "Bear Facts/PandaFacts.txt",
    "teddy": "Bear Facts/TeddyFacts.txt",
}

@app.post("/uploadfile/")
async def process_image(image: UploadFile = File(...)):
    allowed_ext = ['jpg', 'jpeg', 'png', 'JPG']
    ext = image.filename.split('.')[-1]
    if ext not in allowed_ext:
        return {"error": "Invalid file type. Please upload an image."}

    try:
        img = Image.open(image.file)
        bear_type = preprocess_image(img)
        file_path = bear_files.get(bear_type, None)
        if not file_path:
            return {"error": "Bear type not recognized."}

        info = {}
        with open(file_path, "r") as file:
            lines = file.readlines()
            info["Name"] = lines[0].split(":")[1].strip()
            info["Scientific Name"] = lines[1].split(":")[1].strip()
            info["Population"] = lines[2].split(":")[1].strip()
            info["Extinction Status"] = lines[3].split(":")[1].strip()
            info["Type"] = lines[4].split(":")[1].strip()
            info["Diet"] = lines[5].split(":")[1].strip()
            info["Location"] = lines[6].split(":")[1].strip()
            facts = []
            for i in range(7, len(lines)):
                fact = lines[i].split(":")[1].strip()
                facts.append(fact)
            info["Facts"] = facts
        # Format the file contents as desired
        # print(info)
        result = info

    except Exception as e:
        return {"error": str(e)}

    return result
