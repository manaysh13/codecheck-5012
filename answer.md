### インターンシップ・ハッカソンでの成果
これまでに３つのインターンシップを経験しました。

##### ベンチャー企業での自然言語処理のR&Dのインターンシップ
キュレーションアプリの開発を主に行っている企業で1ヶ月のインターンシップを行いました。業務内容は、ニュースなどの記事をカテゴリ別に分類するアルゴリズムの改善という内容で取り組ませていただきました。従来では主に文字列マッチングによるスコアリングをベースに記事分類を行っていたのですが、固有表現など多岐に渡るジャンルで用いられる単語が記事分類の誤りを引き起こしてしまうという問題がありました。例えば、「コカ・コーラ」という固有表現の単語が含まれる記事には飲料を示すカテゴリが一般的ですが、中にはスポーツを表すカテゴリもあります。このような事例を適切に分類することを目指し、分散表現と呼ばれる、単語を連続値の意味ベクトルに変換した表現を用いることで上記の課題改善を行いました。その結果、分類精度に改善が見られ、実際のアプリケーションに取り入れられることになりました。

##### 研究所でのインターンシップ
NTTコミュニケーション科学基礎研究所にて「英語問題自動解答システムの構築」というテーマで1ヶ月のインターンシップを行いました。特に英語センター試験の意見要旨把握問題の自動解答というテーマで取り組ませていただきました。従来手法では、分散表現をベースとして文間の類似度を測定することによる手法が取られていましたが、この手法のみだと「good」と「bad」など極性が対照的な表現を識別することが非常に困難です。一方で、意見要旨把握問題を解答する際にはこのような対照的な極性の認識は非常に重要となります。そこで自分の提案手法では文間の極性一致度を考慮したアルゴリズムを提案しました。また、文間の類似度の測定についても、従来の単純な測定ではなく近年の論文で提案された手法を使用し、さらに安定した類似度測定を行いました。これらの提案をした結果、これまでの手法と同等もしくはそれ以上の精度を出すことができ、提案手法の有用性を示すことができました。

##### Web系企業でのインターンシップ
リクルートホールディングスにてデータ分析のインターンシップを二週間させていただきました。業務内容の詳細はお伝えできないですが、実際にログとして溜まっているデータの解析をさせていただきました。自分の研究で扱っているデータとは大きく異なり、とても綺麗とは言い難いデータに触れさせていただき、実際の業務を行う上で、前処理や例外処理などを丁寧に行う必要性を学びました。また、チームでの作業だったため、集団開発の方法など、それまで自分がしたことのない経験をさせていただきました。


---

### 学部時代の研究テーマについて
学部時代の研究として、難しい言い回しなどが文に含まれていて読解することが困難な難解文をより平易な文に言い換えを行うテキスト平易化という分野について研究を行っていました。先行研究の枠組みでは効果的な言い換えができていなかった問題を深層学習ベースの手法を用いることにより、適切な言い換えが可能になるように試みました。また、深層学習の手法の問題点である低頻度語の扱いについて、固有表現抽出の技術を用い、問題解決を行いました。


---


### 現在の研究テーマについて
言語処理における構文解析のタスクについて主に取り組んでいます。このタスクは与えられた文がどのような構造を持っているかを解析する分野であり、機械翻訳や情報抽出などの応用的な技術を支える技術であり、高い精度が求められています。
近年の手法では深層学習をベースとした手法がかなり高い精度を出しており、非常に単純な学習方法やデコードの方法であっても高精度になることが報告されています。そこで私の研究では、従来研究されていた構造学習の手法を深層学習の枠組みに組み入れることによって、さらなる精度改善を狙うことを行っています。
また、自分の提案手法を実装するにあたり、深層学習のフレームワークを用いたネットワークの実装だけでなく、フレームワーク内では実装するのが困難な構造があります。そのような部分はフレームワークを拡張してコーディングを行ったり、必要な部分のアルゴリズムを1から自前で実装したりしています。
現在、今後の国内の学会や国際会議への投稿を目指して、取り組んでいます。
