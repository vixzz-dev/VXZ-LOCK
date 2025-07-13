pkg update -y && pkg upgrade -y  
pkg install python -y  
pkg install git -y  
git clone https://github.com/vixzz-dev/VXZ-LOCK.git  
cd VXZ-LOCK  
pip install requests bs4 colorama  
python vxzlock.py  
