# Blender Live Export Addon with Browser Viewer

This repository contains two files:
- **`viewer.html`**: A Three.js-based viewer to visualize your Blender scene in a web browser.
- **`live_export.py`**: A Blender addon that exports your Blender scene live to the viewer on every save (`Ctrl+S`).

---

## Features
- Export Blender scenes live with applied modifiers.
- View your scene in a browser with an environment texture and model visualization.
- Customize the background with a toggle to show/hide the environment texture or set a custom color.

---

## Tutorial Video

Watch the tutorial video below to learn how to install and use this addon:

[![Watch the tutorial on YouTube](https://img.youtube.com/vi/IpxbGt_pQ6Q/0.jpg)](https://www.youtube.com/watch?v=IpxbGt_pQ6Q)

Click the image above or [watch it on YouTube](https://www.youtube.com/watch?v=IpxbGt_pQ6Q).

---
## Installation and Usage

### 1. Clone or Download the Repository
Clone or download this repository to your local machine:
```bash
git clone https://github.com/soroushaz1/BlenderLiveViewer.git
```

Or download the repository as a ZIP file and extract it.

### 2. Copy `viewer.html` to Blender's Installation Path
Copy the `viewer.html` file to your Blender installation path. For example:

- **Windows**: `C:\Program Files\Blender Foundation\Blender <version>\`
- **Mac**: `/Applications/Blender.app/Contents/Resources/`
- **Linux**: `/usr/share/blender/<version>/`

This makes it accessible to the HTTP server started by the addon.

**Important:** You must run Blender as an administrator for the addon to work correctly, as it requires permission to start a local HTTP server and write files.

### 3. Install the Blender Addon
1. Open Blender.
2. Go to **Edit > Preferences > Add-ons**.
3. Click **Install** and navigate to the `live_export.py` file in this repository.
4. Enable the addon by checking the box next to `Live Export for Browser`.

### 4. Enable Live Export
1. Go to the **Scene Properties** tab in the Blender Properties panel.
2. You’ll see a new section called **Live Export to Browser**.
3. Click the **Toggle Live Export** button to enable live exporting. The addon will:
   - Export the scene to a `.glb` file every time you save the Blender file (`Ctrl+S`).
   - Start a local HTTP server on port `8000`.


### 5. Open the Viewer
Open your browser and navigate to:
```
http://localhost:8000/viewer.html
```

This will load the `viewer.html` file, allowing you to interact with your Blender scene.

---

## Viewer Features
- **Environment Texture**: Displays the scene's environment texture as a background.
- **Custom Background Color**: Use the color picker to set a solid background color.
- **Background Toggle**: Show or hide the environment texture.

---

## Notes
- The environment texture must be set in Blender's **World Properties** and connected to an `Environment Texture` node for it to be exported and displayed in the viewer.
- Make sure you save your Blender file (`Ctrl+S`) to trigger the export.
- This addon has been tested and works with Blender version 3.6.1. Compatibility with other versions may vary.
---

## Troubleshooting
- **Viewer is Blank**:
  - Ensure the `viewer.html` file is in the correct location and accessible at `http://localhost:8000/viewer.html`.
  - Check if the HTTP server is running (messages appear in the Blender console).
- **Environment Texture Not Visible**:
  - Ensure an `Environment Texture` node is connected in the World Properties of the Blender scene.
- **Addon Fails to Start**:
  - Make sure you are running Blender as an administrator. This is required to start the local HTTP server and save files in restricted directories.

---
