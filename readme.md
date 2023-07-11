## Individual-Based Biological Model inspired by the movie "The Platform"

---
### 内容

映画　The Platform を観て思いついたモデル。  
ある条件下で人間性の進化を追う。
人間性は「生存に不要な食料」を”必要分以上食べてしまうかどうか”、だと定義した。

---
### 動作環境

@macOS Big Sur 11.5.2  
Intel Core i5  
memory 8GB  

---
### ツール
Python 3.9.10  
- pip 22.2  
    - matplotlib

---
### 必要なファイル
- func.py  
- main.py  
- setting.py

---
### 使い方

1. 準備

    以下のコマンドで必要なツールをダウンロードする。
    
    ```
    python3 -m pip install matplotlib
    ```

1. 以下のコマンドで実行する。

    ```
    python3 main.py
    ```

---
### 解析内容

本解析では複数回エサの量を変えながらサイクルを回し、エサの量によって人間性がどのように変化するか検討する。

設定では以下の2点を設定する。
- 1サイクルで設定する階層の深さ（深いほど下は餌の量が少なくなる)
- 全部で何サイクル回すのか