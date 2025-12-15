# Prompt to Image using OpenAI DALL-E

This project generates images from text prompts using OpenAI's DALL-E 3 model. It takes a user prompt, creates an image, downloads it, and saves it as a PNG file.

## Features

- Generate a single 1024x1024 image from a text prompt
- Download and save the image locally as `image.png`
- Display the image (if supported by the environment)

## Requirements

- Python 3.8+
- OpenAI API key with DALL-E access
- Required packages: `openai`, `pillow`, `requests`

## Setup

1. Clone or download the project.

2. Create a virtual environment:
   ```
   python -m venv .venv
   ```

3. Activate the virtual environment:
   - Windows: `.venv\Scripts\activate`
   - macOS/Linux: `source .venv/bin/activate`

4. Install dependencies:
   ```
   pip install openai pillow requests
   ```

5. Set your OpenAI API key as an environment variable:
   ```
   export OPENAI_API_KEY="your-api-key-here"
   ```
   Or on Windows PowerShell:
   ```
   $env:OPENAI_API_KEY = "your-api-key-here"
   ```

## Usage

Run the script:
```
python main.py
```

Enter your image prompt when prompted. The script will generate the image, download it, and save it as `image.png` in the current directory.

## Notes

- Ensure your OpenAI account has credits and DALL-E 3 access.
- Image generation may take a few seconds.
- The `img.show()` call attempts to display the image; it may not work in headless environments.
1. Add API Key

Create .env file:

OPENAI_API_KEY=your-openai-api-key


Or export manually:

export OPENAI_API_KEY="your-key"

2. Run the script
python dalle_video.py


You will be asked:

Enter your video prompt:


Example input:

A futuristic cyberpunk city with neon lights and flying cars

▶️ Output Example

Your project will generate:

12 PNG frames

1 MP4 video (dalle_video.mp4)

The frames create a smooth simulated motion animation.

🧠 How It Works (Simplified)
1. Frame Generation
response = client.images.generate(
    model="dall-e-3",
    prompt=full_prompt,
    n=1,
    size="1024x1024"
)

2. Images Downloaded Locally
frame_000.png
frame_001.png
...
frame_011.png

3. OpenCV Builds Video
video = cv2.VideoWriter("dalle_video.mp4", fourcc, FPS, (width, height))

📝 Example Prompt Ideas

Try prompts like:

“Waterfall jungle landscape, cinematic drone motion”

“Astronaut walking on Mars during sunset”

“Product showcase: rotating perfume bottle, studio lighting”

“Cozy room with gentle camera movement”

“Anime character floating in glowing particles”

📜 License

MIT License — free for personal and commercial use.