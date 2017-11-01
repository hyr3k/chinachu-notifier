# chinachu-notifier
Chinachuの録画をどこかに通知するやつ。

Slackしか対応してないけど気が向いたらやりそう。

## 使い方

1. Python3をインストール
2. このレポジトリをclone `git clone https://github.com/hyr3k/chinachu-notifier`
3. `config.ini.example` をリネームし `config.ini` を作って設定を記載
4. Chinachuの `config.json` に `recordedCommand` を追加

追加例: `"recordedCommand": "/home/chinachu/chinachu-notifier/chinachu-notifier.py",`
