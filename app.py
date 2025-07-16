from flask import Flask, request, render_template, send_from_directory
from diffusers.pipelines.stable_diffusion.pipeline_stable_diffusion import StableDiffusionPipeline
import torch
import os
import uuid

app = Flask(__name__)
app.config['GENERATED_FOLDER'] = 'static/generated'
os.makedirs(app.config['GENERATED_FOLDER'], exist_ok=True)

pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
)
pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")


@app.route('/', methods=['GET', 'POST'])
def index():
    image_filename = None
    if request.method == 'POST':
        prompt = request.form.get('prompt')
        if prompt:
            image = pipe(prompt).images[0]
            filename = f"{uuid.uuid4().hex}.png"
            path = os.path.join(app.config['GENERATED_FOLDER'], filename)
            image.save(path)
            image_filename = filename
    return render_template('index.html', image_filename=image_filename)


@app.route('/generated/<filename>')
def serve_image(filename):
    return send_from_directory(app.config['GENERATED_FOLDER'], filename)


if __name__ == '__main__':
    app.run(debug=True)
