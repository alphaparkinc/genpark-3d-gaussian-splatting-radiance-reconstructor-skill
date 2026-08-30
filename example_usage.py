from client import GaussianSplatting3dRadianceReconstructorClient

def main():
    client = GaussianSplatting3dRadianceReconstructorClient()
    res = client.reconstruct_3d_splat('https://assets.genpark.ai/video/historic_cathedral.mp4', 1500000)
    print('3D Gaussian Splatting Reconstructor: ' + res['reconstruction_job_id'])
    print('Gaussians: ' + str(res['gaussians_trained_count']) + ' | PSNR Quality: ' + str(res['psnr_reconstruction_quality_db']) + ' dB')
    print('Render Rate: ' + str(res['realtime_rendering_fps_metal_cuda']) + ' FPS | SH Degree: ' + str(res['sh_spherical_harmonics_degree']))
    print('PLY URL: ' + res['splat_ply_export_url'])

if __name__ == '__main__':
    main()
