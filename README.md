# 3D_Print_Data-MiniTrashCan
卓上ゴミ箱の3D プリント用データ(Solid Python code)です。
![IMG_0197](https://user-images.githubusercontent.com/54632092/135736849-b1a5c5c9-70b1-4c06-b88d-4eed26f21130.JPG)

# environment
* [SolidPython](https://solidpython.readthedocs.io/en/latest/#)
* [OpenSCAD](https://openscad.org/)

# deploy
1. source code(TrashCan.py)をSolidPython[^1]でビルド。出力ファイルの中身をコピー。
[^1]:著者はGoogle Colaboratoryにて、SolidPythonをインストールしてビルドを実行した。<br>インストールのコマンドは```!pip install SolidPython```
2. OpenSCADのEditor画面にペースト。Editorの1行目に```$fn=36;```[^2]を追加した上で、STLファイルを作成。
[^2]:OpenSCADが円弧を36分割して演算してくれるので、カクカクなのが滑らかになる。数値を大きくするほど滑らかになるが、演算に時間がかかる。
3. 3Dプリンターで印刷。

# reference
* インターフェース 2021年10月号 
<img src="https://user-images.githubusercontent.com/54632092/135737217-b3234d6c-6947-4455-bb65-33e6a8fba5e8.jpg" width=25% >

* ゴミ箱本体図面
![trash_can](https://user-images.githubusercontent.com/54632092/136641318-b712534d-65a8-4c67-98b3-fd3356cc9ab4.png)

* 蓋図面
![trash_can_lid](https://user-images.githubusercontent.com/54632092/136641402-08454136-66cf-4a98-bbc2-740c53b7d0ef.png)
