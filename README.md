# Cài đặt Git LFS
git lfs install

# Theo dõi các tệp .pkl bằng Git LFS
git lfs track "*.pkl"

# Thêm và commit lại các tệp lớn
git add .gitattributes


git add .
git commit -m "Using Git LFS"

git branch -M main
git remote add origin https://github.com/phamthanhlam0201/Lab5-DS102-Classify_Image_Chest_Xray.git

git push -u origin main


Link data: 
    https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia

Install library:
    pip install flask
    pip install joblib

Run app:
    python app.py


