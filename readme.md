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

    ```
    # move to execute directory
    cd /Users/toma/GitHub/the_platform

    # activate venv
    source venv/bin/activate    
    
    # install python libraries
    pip install -r requirements.txt
    ```

1. 実行

    ```
    bash main.sh
    ```

---
### 解析内容

まず以下を設定する。
- ステージ数（int）
- ラウンド数（int）
- 実験回数（>1, int）

ステージは以下を持っている。
- 胃袋の大きさ（0-1, float）
- 満たされ具合（0-1, float）
- 食欲（0-1, float）
満たされ具合×食欲分食べる。

残ったエサが次のステージに落ちる。

全ステージを通ったら１ラウンド終了。

ラウンド後、ステージを組み替える。