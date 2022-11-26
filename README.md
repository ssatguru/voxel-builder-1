# Voxel Builder

![banner](https://repository-images.githubusercontent.com/565157149/7f80ff43-9a88-4e87-96b3-6a0ccc1f13dc "banner")

Voxel-based 3D modeling application<br>
**3.8.5 Beta 2022**

[ [Try now](https://nimadez.github.io/voxel-builder) ] [ [Changelog](https://github.com/nimadez/voxel-builder/blob/main/CHANGELOG) ]

## Features

Model, Bake and Render

- File I/O, import and export *(drag and drop)*
- Quick save and load, 10 memory steps *(undo/redo)*
- Terrain, city, cube, plane and isometric room generators
- OBJ and image voxelization *(JPG, PNG, SVG)*
- Symmetric drawing and painting, symmetrize and mirror
- Marquee selection tool, hide/paint/bake/delete by selection
- Bake voxel particles into clean mesh
- Clone and replicate bakes and parts
- Realistic rendering, PBR material, HDR image
- Color palette and color pickers
- Asset viewer *(OBJ, GLB, STL, FBX, HDR, EXR)*
- Axis view *(view cube)*
- Dynamic scene grid
- WASD controls on desktop
- Joystick controls for touchscreen
- Clean handcrafted user interface

##### ***Check "Help" menu for details***

##### ***Supported Platforms***
- Electron *(recommended)*
- Google Chrome for desktop
- Google Chrome for mobile devices *(partially)*
<br><sub>* *Tablet recommended for best experience*</sub>

## Known Issues
```
[ Voxel is a Particle ]
Each voxel is a particle, we used particles to build the world!
Pros: higher performance on desktop and mobile
Cons: unable to remove shared faces, hard to manage particles

[ Max. 64,000 Voxel Particles ]
Unable to use the browser's local-storage after 64000 voxels,
this will affect the quick save and load, memory steps and
overall browser performance on desktop and mobile devices.
One possible option is to store data in chunks, but not
worth the complexity in a single html file.
Solution: use Bakery, 64000 voxels per bake!

[ Drawing on The Floor ]
It is possible to enable the floor drawing, but it makes
navigation more painful, especially on touch devices,
you may drawing instead of rotating the camera!
Solution: use New Floor to start with a floor

[ The Challenge ]
Minimum dependency, a single HTML file < 500KB!
```

## History
```
3.8.0 -> advancing to the next level
3.6.0 -> major code rewrite
3.4.0 -> new features and ui/ux overhaul
3.0.0 -> SPS particles to build the world
```

###### 3.0.0 *(BJS 4)* to 3.8.0<br>
![screenshot](media/devshots.jpg?raw=true "Screenshot")

## License
Code released under the [MIT license](https://github.com/nimadez/voxel-builder/blob/main/LICENSE).

## Credits
- [Babylon.js](https://www.babylonjs.com/)
- [Three.js](https://threejs.org/) *(asset-viewer and vi²xel)*
- [Electron](https://www.electronjs.org/)
- [Google Material Icons](https://github.com/google/material-design-icons)
- [Droid Sans Font](https://www.android.com/)
- [Blender](https://blender.org/)
- [KhronosGroup glTF-Sample-Models](https://github.com/KhronosGroup/glTF-Sample-Models)
- [KhronosGroup glTF-Sample-Environments](https://github.com/KhronosGroup/glTF-Sample-Environments)
- [jsDelivr](https://www.jsdelivr.com/)

###### This project is available at [Babylon.js Demos](https://www.babylonjs.com/community/) and [Babylon.js Forum](https://forum.babylonjs.com/t/voxel-builder-voxel-based-3d-modeling/)
