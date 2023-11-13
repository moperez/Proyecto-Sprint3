echo. ##############TEST PATH ############# 
cd ./Tests 
python -m pytest tst_001.py tst_002.py tst_003.py --html=../Results/PerezFariasCecilia.html --self-contained-html 
pause
