!pwd
target_path = "/content/drive/My Drive/pytorch-CycleGAN-and-pix2pix-master/checkpoints/summer2winter_pix2pix/"
structureD = "_net_D.pth"
structureG = "_net_G.pth"

i = 24

os.rename(target_path + str(i) + "_net_D.pth" , target_path + "latest_net_D.pth")
os.rename(target_path + str(i) + "_net_G.pth" , target_path + "latest_net_G.pth")
os.mkdir("./results/" + str(i))
!python test.py --dataroot "/content/drive/My Drive/pytorch-CycleGAN-and-pix2pix-master/datasets/summer2winter/" --direction AtoB --model pix2pix --name summer2winter_pix2pix --results_dir "./results/24/"
os.rename(target_path + "latest_net_D.pth" , target_path + str(i) + "_net_D.pth")
os.rename(target_path + "latest_net_G.pth" , target_path + str(i) + "_net_G.pth")
