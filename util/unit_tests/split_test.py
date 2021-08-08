import glob
base_path = '/home/paulo/openvslam/openvslam/build/'
video_names = glob.glob(base_path+'/{}/videos/*.MP4'.format('testes')) # Get video names list  
mask_list = glob.glob(base_path+'/unit-test/masks/*.png')

resolution = 1080
# mask_valid = []
# mask_names = []
# for mask in mask_list:
#     mask_name = mask.split('/')[-1]
#     if(mask_name.startswith('mask{}'.format(resolution))):
#         mask_valid.append(mask)
#         mask_names.append(mask.split('/')[-1])
#     print(mask_names)

mask_valid = []    
mask_names = []

frameskip_list = [0,1,2,3,4,5,6]
for mask in mask_list:
    mask_name = mask.split('/')[-1]
    if(mask_name.startswith('mask{}'.format(resolution))):
        mask_valid.append(mask)
        mask_names.append(((mask.rsplit( ".", 1 )[ 0 ]).split('/')[-1]).split('-')[-1])
        print(mask_valid)
        # obter o argumento da mascara

        #print('Mascara obtida {}'.format((mask.rsplit( ".", 1 )[ 0 ]).split('/')[-1]).split('-')[-1])
for video in video_names:
    for frameskip in frameskip_list:
        for mask in mask_valid:
            fps =  int(120/(1+frameskip))
            mask_size = (((mask.rsplit( ".", 1 )[ 0 ]).split('/')[-1]).split('-')[-1])
            file_name = ((video.rsplit( ".", 1 )[ 0 ]).split('/')[-1]).split('-')[0]
            map_name = [file_name,str(fps),str(resolution),str(mask_size)]
            map_name = ('-').join(map_name)
            #video_name = video_name.
            #map_name = video_name.split('-')[:-1]
            print(map_name)
