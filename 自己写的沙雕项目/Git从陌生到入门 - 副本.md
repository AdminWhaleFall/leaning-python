# Git概述

> Git 是 Linus Torvalds 为帮助管理 Linux 内核开发而开发的开放源代码的版本控制软件，由 C语言编写。

## 版本控制系统

Git 是目前最先进的版本控制系统。（不是之一，就是最先进的）

#### 概念

现在，让我们做一个假设：你给心爱的女生写了一封情书，仔细一想，你并不想就这样草率地交给她，于是更改了很多地方，但你怕将来想把删掉的段落加回来，于是在这个文件夹创建了一个副本，然后再进行更改。

最后你的文件夹中是这样的：

| 名称                    | 修改日期        | 类型                | 大小  |
| :---------------------- | --------------- | ------------------- | :---- |
| 情书.doc                | 2021/1/26 13:39 | Microsoft Word 文档 | 521KB |
| 情书-副本.doc           | 2021/1/26 13:40 | Microsoft Word 文档 | 520KB |
| 情书最终版.doc          | 2021/1/26 14:32 | Microsoft Word 文档 | 521KB |
| 情书最终版-副本.doc     | 2021/1/26 14:58 | Microsoft Word 文档 | 520KB |
| 情书终极不变版.doc      | 2021/1/26 15:20 | Microsoft Word 文档 | 521KB |
| 情书终极不变版-副本.doc | 2021/1/26 15:50 | Microsoft Word 文档 | 521KB |
| ……                      | ……              | ……                  | ……    |

你想找回原来写的一段更好的话，但是你已经忘了是在哪个文件中了，只能一个一个去找。

看着乱七八糟的一大堆文件，你想删掉一个，但又怕把一段重要的话丢掉，只能留着他们。

好，那么现在你就需要一个梳理各个版本的系统，在经过整理后，不但可以记录每次文件的改动，也不需要整理乱七八糟的文件，甚至还可以让好基友帮你参考改进！

这个控制系统用起来应该是这样：

| 版本 | 文件名  | 用户     | 说明                           | 日期       |
| ---- | ------- | -------- | ------------------------------ | ---------- |
| 1.0  | 情书.md | 文艺青年 | 加入了一张图片                 | 1/26 13:39 |
| 2.0  | 情书.md | 文艺青年 | 删除了“我在初中第一次见你”整段 | 1/26 13:40 |
| 3.0  | 情书.md | 文艺青年 | 删除了"我在高中第一次见你"整段 | 1/26 14:32 |

#### 集中式与分布式

- Linus 十分痛恨集中式的版本控制系统：

  版本库是集中存放在**中央服务器**上的，在工作时，需要成员将最新版本的工程下载到自己的电脑中，肝完以后再把工作推送给中央服务器。这就要求成员必须联网才能正常工作，而且如果遇到网络不佳的情况，或是代码量庞大的项目，则更加麻烦。

- 分布式版本控制系统则与集中式有很大区别：

  - 分布式版本控制系统**没有中央服务器**，每一个成员的电脑上都有一个完整的版本库。所以你在工作时并不需要联网，因为这整个版本库就在你的电脑上。
  - 在多人协作时，若你和你的基友同时修改了"情书.md"，你们只需要将各自的文件推送给对方，这样两者都可以看到更改了。
  - 分布式版本控制系统的安全性更高。若一个成员的电脑坏掉了，那么很简单，修好电脑再从其他人的电脑中clone一个过来即可，而集中式的服务器坏掉的话，后果就不用多说了。

- > Git 和其它版本控制系统的主要差别在于 Git 对待数据的方式：
  >
  > 从概念上来说，其它大部分系统以**文件变更列表**的方式存储信息，这类系统将它们存储的信息看作是一组基本文件和每个文件随时间逐步累积的差异 （它们通常称作 基于差异（delta-based） 的版本控制）。
  >
  > 而 Git 不按照以上方式对待或保存数据。反之，Git 更像是把数据看作是对小型文件系统的一系列**快照**。 在 Git 中，每当你提交更新或保存项目状态时，它基本上就会对当时的全部文件创建一个快照并保存这个快照的**索引**。 为了效率，如果文件没有修改，Git 不再重新存储该文件，而是只保留一个链接指向之前存储的文件。 Git 对待数据更像是一个 **快照流**。
  >
  > 这是 Git 与几乎所有其它版本控制系统的重要区别。 因此 Git 重新考虑了以前每一代版本控制系统延续下来的诸多方面。 Git 更像是一个小型的文件系统，提供了许多以此为基础构建的超强工具，而不只是一个简单的 VCS。 稍后我们在[Git 分支](https://git-scm.com/book/zh/v2/ch00/ch03-git-branching)讨论 Git 分支管理时，将探究这种方式对待数据所能获得的益处。
  >
  > ——引自[Git官方网站](https://git-scm.com/book/zh/v2/%E8%B5%B7%E6%AD%A5-Git-%E6%98%AF%E4%BB%80%E4%B9%88%EF%BC%9F)

## Git工作流程

三种状态：

|状态|描述|
| ---------------- | -------------------------------------------- |
| 已修改(modified) | 已修改表示修改了文件，但还没保存到数据库中。 |
| 已暂存(staged) | 已暂存表示对一个已修改文件的当前版本做了标记，使之包含在下次提交的快照中。 |
| 已提交(committed) | 已提交表示数据已经安全地保存在本地数据库中。 |

 这三种状态会让我们的项目拥有三个阶段：

| 阶段（区） | 描述                                                         |
| ---------- | ------------------------------------------------------------ |
| 工作区     | 工作区是对项目的某个版本**独立提取**出来的内容。 这些从 Git 仓库的压缩数据库中提取出来的文件，放在磁盘上供你使用或修改。 |
| 暂存区     | 暂存区是一个文件，保存了**下次将要提交的文件列表信息**，一般在 Git 仓库目录中。 按照 Git 的术语叫做“索引”，不过一般说法还是叫“暂存区”。 |
| Git 目录   | Git 仓库目录是 Git 用来**保存项目的元数据**和对象数据库的地方。 这是 Git 中最重要的部分，从其它计算机克隆仓库时，复制的就是这里的数据。 |

**基本的 Git 工作流程如下**：

1. 在工作区中修改文件。
2. 将你想要下次提交的更改，将更改的部分添加到暂存区。
3. 提交更新，找到暂存区的文件，将快照永久性存储到 Git 目录。

## 其它

- Git 可以保证文件的完整性：

  [哈希值](https://baike.baidu.com/item/%E5%93%88%E5%B8%8C%E5%87%BD%E6%95%B0/9796422?fromtitle=%E5%93%88%E5%B8%8C%E5%80%BC&fromid=5896926&fr=aladdin)作为校验依据，在传送过程中丢失信息或损坏文件时，Git可以发现这种情况，中断这个过程。

- Git 只可以添加数据，几乎不会执行任何可能导致文件不可恢复的操作，也就是说，不会让你删除任何一个文件，除非你删掉了整个仓库。

# Git基础

## 设置Git

1. 下载并安装最新版本的Git

   [MacOS](https://git-scm.com/download/mac)

   [Windows](https://git-scm.com/download/win)

   [Linux/Unix](https://git-scm.com/download/linux)

2. 在Git中设置用户名

   - **为每个仓库设置用户名**

     打开终端。（Windows可以打开Git Bash）

     设置Git用户名：

     ```shell
     $ git config --global user.name "BeyoundClouds"
     ```

     确认你设置了正确的Git用户名：

     ```shell
     $ git config --global user.name
     > BeyoundClouds
     ```

   - **为单个仓库设置用户名**

     打开终端。

     将当前工作目录更改为您想要在其中配置与 Git 提交关联的名称的本地仓库。

     后续步骤同上。

3. 设置提交邮件电子地址

   - 在代码托管平台设置

     请参考后续的 ”Git 远程仓库“

   - 在Git中设置

     打开终端

     在 Git 中设置电子邮件地址：

     ```shell
     $ git config --global user.email "test@beyondclouds.com"
     ```

     确认在 Git 中正确设置了电子邮件地址：

     ```shell
     $ git config --global user.email
     test@beyondclouds.com
     ```

     将电子邮件地址添加到代码托管平台，以便于区分提交者。 每一个 Git 提交都会使用这些信息，它们会写入到你的每一次提交中，不可更改。

     如果使用了 --global 选项，那么该命令只需要运行一次，之后你做任何事情， Git 都会使用那些信息。 

     当你想针对特定项目使用不同的用户名称与邮件地址时，可以在那个项目目录下运行没有 --global 选项的命令来配置。

4. 至此，你已经完成了 Git 的基础设置。

## Git 使用

下面的内容涵盖了你在使用 Git 时将会用到的各种基本命令。

你可以学习到配置并初始化一个仓库（repository）、开始或停止跟踪（track）文件、暂存（stage）或提交（commit）更改。 

你也可以知道如何配置 Git 来忽略指定的文件和文件模式、如何迅速而简单地撤销错误操作、如何浏览你的项目的历史版本以及不同提交（commits）之间的差异、如何向你的远程仓库推送（push）以及如何从你的远程仓库拉取（pull）文件。

### 创建 Git 仓库

创建仓库有两种方法：

1. 将尚未进行版本控制的本地目录 **转换** 为 Git 仓库。
2. 从其它服务器 **克隆** 一个已存在的 Git 仓库。

- **在已存在目录中初始化仓库**

  首先需要进入该项目目录中：

  ```shell
  $ cd /my_project
  ```

  之后执行：

  ```shell
  $ git init
  ```

  该命令将创建一个名为 .git 的子目录，这个子目录含有你初始化的 Git 仓库中所有的必须文件，这些文件目前不需要掌握。 但是我们仅仅做了一个初始化的操作，你项目中的文件还没有被跟踪。

  现在，你已经得到了一个初始的 Git 仓库。

- **克隆现有的仓库**（HTTPS协议）

  克隆仓库的命令是` git clone `。当你执行 `git clone` 命令的时候，默认配置下远程 Git 仓库中的每一个文件的每一个版本都将被拉取下来存到你的电脑上。

  克隆仓库的命令格式为：

  ```shell
  git clone <repo> //repo是Git仓库的https链接
  ```

  如果我们需要克隆到指定的目录，可以使用以下命令格式：

  ```shell
  git clone <repo> <name> //name是你要自定义的名称
  ```

### 提交与修改文件

Git 的工作就是创建和保存你的项目的快照及与之后的快照进行对比。

**再次强调，提交文件的步骤为**：

1. 先在本地修改，编辑。
2. 将文件存放到暂存区。
3. 将暂存区的文件放入到Git仓库中。

下面用一个表来列出基础的命令：

| 命令         | 说明                                   |
| ------------ | -------------------------------------- |
| `git add`    | 将文件添加到暂存区。                   |
| `git status` | 查看仓库当前的状态，显示有变更的文件。 |
| `git diff`   | 比较文件的不同。                       |
| `git commit` | 提交暂存区到本地仓库。                 |
| `git reset`  | 回退版本。                             |
| `git rm`     | 删除工作区文件。                       |
| `git mv`     | 移动或重命名工作区文件。               |

- `git add`

  这个命令可以将文件添加到暂存区。

  每次文件被修改后，需要使用`git add`命令来再次提交更改。

  普通用法：

  ```shell
  $ git add test
  //将test文件加入到了暂存区
  ```

  此命令可以添加多个文件，中间用空格隔开即可：

  ```shell
  $ git add file01 file02 file03 ...
  //将file01、file01、file03等等一起添加到暂存区
  ```

  添加整个目录：

  ```shell
  $ git add /home/user/OS/test0x00/
  //将整个 "/home/user/OS/test0x00/" 目录添加到暂存区
  ```

  添加当前目录下所有文件：

  ```shell
  $ cd /home/users/OS/test0x01/
  $ git add .
  //将 "/home/users/OS/test0x01/"目录中所有文件添加到了暂存区
  ```

- `git status`

  此命令用于查看在你上次提交之后是否有对文件进行再次修改。

  现在，我干了三件事：

  1. 我在目录下创建了一个 “helloGit.c” 文件，并使用`git add`向主分支提交了更改。

  2. 在此之后我又对 “helloGit.c” 进行了修改。

  3. 然后创建了一个newFile.md ，没有使用`git add`命令提交更改。

  此时，运行`git status`命令后，会输出如下内容：

  ```shell
  $ git status
  On branch master
  
  No commits yet
  //下面一部分表示已经提交更改的文件，即已经在主分支内的文件，这是前面第件事的结果。
  Changes to be committed:		
    (use "git rm --cached <file>..." to unstage)
          new file:   helloGit.c
  //下面一部分表示已经进行了修改，但尚未提交更改的文件，这是第二件事的结果，我在第一步提交之后又对这个文件进行了修改，并没有提交。
  //可以使用 "git commit" 来将更改提交给主分支
  Changes not staged for commit:
    (use "git add <file>..." to update what will be committed)
    (use "git restore <file>..." to discard changes in working directory)
          modified:   helloGit.c
  //下面是没有追踪的文件，即没有添加的文件，可以使用 "git add" 来将这个文件列入追踪范围，即添加到暂存区
  Untracked files:
    (use "git add <file>..." to include in what will be committed)
          newFile.md
  
  ```

- `git commit`

  这个命令用来提交暂存区到本地仓库。

  常规用法：

  ```shell
  $ git commit -m <message>
  //将整个暂存区提交到主分支中
  //message 是一些备注信息，可以记录每次提交修改的版本
  ```

  提交指定的文件到仓库区：

  ```shell
  $ git commit file01 file02 -m ohhhh
  //将file01和file02提交到主分支，并备注ohhhh
  ```

  在修改文件后，如果直接用`git commit`命令的话，是不可行的，因为修改后的文件还没有上传到暂存区，这时可以使用 `-a` 参数:

  ```shell
  $ git commit -a file
  //这一步可以直接将修改过的文件跳过add 命令（或是说自动执行一次add），将文件上传到主分支
  ```

  现在我们将之前的文件全部提交：

  ```shell
  $ git commit -m '第一次提交'
  [master (root-commit) 2614b7d] 第一次提交
   1 file changed, 7 insertions(+)
   create mode 100644 helloGit.c
  ```

  执行`git status`来看看效果：

  ```shell
  $ git status
  On branch master
  nothing to commit, working tree clean
  ```

- `git diff`

  比较文件的不同，即比较文件在暂存区和工作区的差异。

  显示已写入暂存区和已经被修改但尚未写入暂存区文件的区别。

  显示暂存区和工作区的差异:

  ```shell
  $ git diff <file> 	//file为文件名
  ```

  显示暂存区和上一次提交(commit)的差异:

  ```shell
  $ git diff --cached <file>	
  或
  $ git diff --staged <file>	//file为文件名
  ```

  显示两次提交之间的差异:

  ```shell
  $ git diff <first-branch>...<second-branch>
  ```

  **示例：**

  我们在文件 “newFile” 中加入一些东西：

  ```shell
  $ echo 'aaaaa' > newFile.md
  ```

  执行`git diff`:

  ```shell
  $ git diff
  warning: LF will be replaced by CRLF in newFile.md.
  The file will have its original line endings in your working directory
  diff --git a/newFile.md b/newFile.md
  index 6434b13..ccc3e7b 100644
  --- a/newFile.md
  +++ b/newFile.md
  @@ -1 +1 @@
  -This is a new file.
  +aaaaa
  ```

- `git reset`

  用于回退版本，语法格式如下：

  ```shell
  $ git reset <--soft | --mixed | --hard> <HEAD>
  ```

  `--mixed`为默认，可以不用带该参数，用于重置暂存区的文件与上一次的提交(commit)保持一致，工作区文件内容保持不变。

  ```shell
  git reset  <HEAD>
  ```

  实例：

  ```shell
  $ git reset HEAD^            	
  //回退所有内容到上一个版本  
  $ git reset HEAD^ helloGit.c  	
  //回退 helloGit.c 文件的版本到上一个版本  
  $ git reset 052e          	 	
  //回退到指定版本
  ```

  [更多用法](https://www.runoob.com/git/git-reset.html)

- `git mv`

  用于移动或重命名一个文件、目录或软连接，与 Linux 的 `mv` 类似。

  ```shell
  $ git mv file newfile
  //将file重命名为newfile（把file原地tp，并改名叫作newfile）
  ```

- `git rm`

  用于删除文件，与 Linux 的 `rm` 类似。

  ```shell
  $ git rm file
  //删除file
  // -r -f 都可以加
  ```

### 查看提交历史

在提交了若干更新，又或者克隆了某个项目之后，你也许想回顾下提交历史。 完成这个任务最简单而又有效的工具是 `git log` 和`git blame`命令。

- `git log`

  该命令可以查看历史提交记录。

  它会按时间先后顺序列出所有的提交，最近的更新排在最上面。该命令会列出每个提交的 SHA-1 校验和、作者的名字和电子邮件地址、提交时间以及提交说明。

  下面我们针对之前的操作，来让`gitlog`列出历史操作记录：

  ```shell
  $ git log
  commit 01b6078d06be25ea1b77b5fa01c14a3850dc49e2 (HEAD -> master)
  Author: DXLin <DXLin666@outlook.com>
  Date:   Tue Jan 26 20:42:28 2021 +0800
  
      ohhhhh
  
  commit 638f664b8d3ed621167d5206974eeb343d60f3e4
  Author: DXLin <DXLin666@outlook.com>
  Date:   Tue Jan 26 20:42:11 2021 +0800
  
      ohhhh
  
  commit 2614b7d1a1bc3583398acb82e1374e7d44a2ffb6
  Author: DXLin <DXLin666@outlook.com>
  Date:   Tue Jan 26 20:40:22 2021 +0800
  
      第一次提交
  ```

  可以用`--oneline`选项来查看历史纪录的简洁的版本：

  ```shell
  $ git log --oneline
  01b6078 (HEAD -> master) ohhhhh
  638f664 ohhhh
  2614b7d 第一次提交
  ```

  除此之外，他还有很多的选项和用法，功能强大，大家可以去[官方文档](https://git-scm.com/book/zh/v2/Git-%E5%9F%BA%E7%A1%80-%E6%9F%A5%E7%9C%8B%E6%8F%90%E4%BA%A4%E5%8E%86%E5%8F%B2)查阅。

- `git blame`

  如果要查看指定文件的修改记录可以使用 `git blame` 命令，格式如下：

  ```shell
  git blame file
  ```

  它可以以列表形式显示修改记录：
  
  ```shell
  $ git blame helloGit.c
  ^2614b7d (DXLin 2021-01-26 20:40:22 +0800 1) #include <stdio.h>
  ^2614b7d (DXLin 2021-01-26 20:40:22 +0800 2) int main()
  ^2614b7d (DXLin 2021-01-26 20:40:22 +0800 3) {
  ^2614b7d (DXLin 2021-01-26 20:40:22 +0800 4)    printf("Hello Git!\n");
  ^2614b7d (DXLin 2021-01-26 20:40:22 +0800 5)    return 0;
  ^2614b7d (DXLin 2021-01-26 20:40:22 +0800 6) }
  638f664b (DXLin 2021-01-26 20:42:11 +0800 7) //123123123123
  ```
  
  

### 远程操作

 远程仓库是指托管在因特网或其他网络中的你的项目的版本库，如Github,GitLab等。 

与他人协作涉及管理远程仓库以及根据需要推送或拉取数据。 管理远程仓库包括了解如何添加远程仓库、移除无效的远程仓库、管理不同的远程分支并定义它们是否被跟踪等等。

#### Git远程仓库（GitLab）

1. 注册并登录GitLab.

2. <img src="https://beyondclouds.oss-cn-beijing.aliyuncs.com/blog/images/2b48e994-7b11-4be9-9864-cec7e2fa5531.png" alt="image-20210126220509930" style="zoom:70%;" />

   创建一个新的项目。

3. <img src="https://beyondclouds.oss-cn-beijing.aliyuncs.com/blog/images/ff3d2741-8a84-49d2-8a17-4796c11720ef.png" alt="image-20210126220937439" style="zoom:67%;" />

   如图，配置好新的项目，点击创建。

4. 以下便是你这个项目/仓库的信息，中间的`http://....`是这个仓库的连接地址。

   你也可以选择SSH协议，但是SSH协议更为复杂，大家可以自行了解，权衡利弊。

   ![image-20210126221333810](https://beyondclouds.oss-cn-beijing.aliyuncs.com/blog/images/c93bf9a5-9f43-49c5-987d-ab74cb3d2f72.png)

5. 这时你的远程仓库已经配置完毕了。

#### 添加远程仓库

- `git remote`

	直接运行`git remote`可以查看你已经配置的远程仓库服务器，命令执行后将列出你指定的每一个远程服务器的简写。 

	> origin 是 Git 给你克隆的仓库服务器的默认命名。

	运行 `git remote add <shortname> <url>` 可以添加一个新的远程 Git 仓库，同时指定一个方便使用的简写，这里我们将前面在GitLab创建的远程仓库添加进来，并给他一个hello的简写：

	```shell
	$ git remote add hello http://coding.yundingshuyuan.com/DX_Lin/HelloGit.git
	```

	再执行`git remote`来查看：
	
	```shell
	$ git remote
	hello
	```
	
	可见我们已经成功地将这个远程仓库添加了进来。
	
	其他选项：
	
	```shell
	$ git remote rm name
	//删除远程仓库
	$ git remote rename old_name new_name
	//修改仓库名
	```

#### 查看远程仓库

- `git remote`

  这个命令可以查看远程仓库的更多信息，应用到我们的实例上：

  ```shell
  $ git remote show hello
  * remote hello
    Fetch URL: http://coding.yundingshuyuan.com/DX_Lin/HelloGit.git
    Push  URL: http://coding.yundingshuyuan.com/DX_Lin/HelloGit.git
    HEAD branch: master
    Remote branch:
      master tracked
    Local ref configured for 'git push':
      master pushes to master (up to date)
  ```

#### 从远程仓库中抓取与拉取

- `git fetch`、`git merge`

  这个命令会访问远程仓库，从中拉取所有你还没有的数据。：

  ```shell
  $ git fetch .....
  ```

  执行完成后，你将会拥有那个远程仓库中所有分支的引用，可以随时合并或查看。

   必须注意该命令只会将数据下载到你的本地仓库，并不会自动合并或修改你当前的工作，你必须手动将其合并入你的工作，下面这个命令可以尝试将提取的数据合并到当前分支：

  ```shell
  $ git merge
  ```

  以上两个命令的组合可以将服务器上的任何更新（假设有人这时候推送到服务器了）合并到你的当前分支。

- `git pull`

  这其实就是上面两步的简写，效果与先执行`git fetch`再执行`git merge`后相同。

#### 推送到远程仓库

- `git push` 

  该命令用于将本地的分支版本上传到远程并合并：

  ```shell
  $ git push <远程主机名> <本地分支名>:<远程分支名>
  //如果本地分支名与远程分支名相同，则可以省略冒号
  $ git push <远程主机名> <本地分支名>
  ```

  以下命令将本地的 master 分支推送到主机 hello 的 master 分支：

  ```shell
  $ git push hello master
  Enumerating objects: 9, done.
  Counting objects: 100% (9/9), done.
  Delta compression using up to 8 threads
  Compressing objects: 100% (6/6), done.
  Writing objects: 100% (9/9), 773 bytes | 386.00 KiB/s, done.
  Total 9 (delta 1), reused 0 (delta 0), pack-reused 0
  To http://coding.yundingshuyuan.com/DX_Lin/HelloGit.git
   * [new branch]      master -> master
  ```

  可以看到，我们的远程仓库的主分支已经有了我们推送的所有文件：

  ![image-20210126224657119](https://beyondclouds.oss-cn-beijing.aliyuncs.com/blog/images/5da8ce20-871b-4389-847c-bc8b2131d947.png)

#### 远程仓库的重命名与移除

- `git remote rename` 

  可以修改一个远程仓库的简写名。 

  例如，将 `hello` 重命名为 `hl`：

  ```shell
  $ git remote rename hello hl
  $ git remote
  hl
  ```

  值得注意的是这同样也会修改你所有远程跟踪的分支名字。 那些过去引用 `hello/master` 的现 在会引用 `hl/master`。

- `git remote remove`、`git remote rm` 

  如果想要移除一个远程仓库：

  ```shell
  $ git remote remove hl
  ```

  一旦你使用这种方式删除了一个远程仓库，那么所有和这个远程仓库相关的远程跟踪分支以及配    置信息也会一起被删除。

### 分支管理

使用分支意味着你可以从开发主线上分离开来，然后在不影响主线的同时继续工作。

之前的例子中我们都位于默认的master分支，也就是主分支中。

下面是三个基本命令：

- 创建分支：`git branch <branchname>`
- 切换分支：`git checkout <branchname>`
- 合并分支：`git merge`

#### 列出分支

- `git branch`

  没有参数时，它会默认列出你本地的分支：

  ```shell
  $ git branch
  * master
  ```

  意思是现在只有一个叫做master的分支，并且前面的星号（*）表示我们现在位于master分支中。

  新建一个分支test1：

  ```shell
  $ git branch test1
  ```

  查看：

  ```shell
  $ git branch
  * master
    test1
  ```

  可见我们成功创建了test1分支，但我们仍位于master分支中，接下来我们转换到test1分支中：

  ```shell
  $ git checkout test1
  Switched to branch 'test1'
  ```

#### 删除分支

- `git branch -d <branchname>`

  删掉分支 test1：

  ```shell
  $ git branch -d test1
  Deleted branch test1 (was 23f0a22).
  ```

  

#### 分支合并

- `git merge`

  一旦某分支有了独立内容，你终究会希望将它合并回到你的主分支。 你可以使用以下命令将任何分支合并到当前分支中去：

  ```shell
  $ git merge
  ```

  应用到实例：

  ```shell
  $ git branch
  * master
    test2
  $ git merge test2
  Updating 01b6078..358d6d2
  Fast-forward
   testfile.md | 1 +
   1 file changed, 1 insertion(+)
   create mode 100644 testfile.md
  ```

  合并完后可以删除分支。

### 标签

如果你达到一个重要的阶段，并希望永远记住那个特别的提交快照，那这个比较有代表性的版本可以用标签来标记发布结点（ `v1.0` 、 `v2.0` 等等）。

#### 创建标签

- `git tag -a`

  其实这个`-a`可以不写，但是它不会记录这个标签的创建时间，创建者，也不会让你添加注解：

  ```shell
  $ git tag -a v1.0 
  ```

  在执行上面的命令后，Git会自动为你打开Vim编辑器，让你写一句标签的注解，就像之前提交时的提交信息一样。

  再执行`git log --decorate --oneline` 时，我们可以再看见之前打的标签：

  ```shell
  $ git log --decorate --oneline
  358d6d2 (HEAD -> master, tag: v1.0, test2) wow
  01b6078 (hello/master) ohhhhh
  638f664 ohhhh
  2614b7d 第一次提交
  ```

  就是第二行的 ”v1.0“！

  我们也可以为以前的版本追加标签：

  ```shell
  $ git tag -a v0.1 2614b7d
  ```

  ```shell
  $ git log --decorate --oneline
  358d6d2 (HEAD -> master, tag: v1.0, test2) wow
  01b6078 (hello/master) ohhhhh
  638f664 ohhhh
  2614b7d (tag: v0.1) 第一次提交
  ```

  

#### 列出所有标签

- `git tag`

  让我们列出刚刚打的所有标签：

  ```shell
  $ git tag
  v0.1
  v1.0
  ```

#### 共享标签

- `git push <主机名> <tag>`

  默认情况下，`git push` 命令并不会传送标签到远程仓库服务器上。

  在创建完标签后你必须显式地推送标签到共享服务器上：

  ```shell
  $ git push hello v1.0
  Enumerating objects: 5, done.
  Counting objects: 100% (5/5), done.
  Delta compression using up to 8 threads
  Compressing objects: 100% (3/3), done.
  Writing objects: 100% (4/4), 468 bytes | 468.00 KiB/s, done.
  Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
  To http://coding.yundingshuyuan.com/DX_Lin/HelloGit.git
   * [new tag]         v1.0 -> v1.0
  ```

  如果想要一次性推送很多标签，也可以使用带有 `--tags` 选项的 `git push` 命令。 这将会把所有不在远程仓库服务器上的标签全部传送到那里。

  ```shell
  $ git push hello --tags
  Enumerating objects: 1, done.
  Counting objects: 100% (1/1), done.
  Writing objects: 100% (1/1), 162 bytes | 162.00 KiB/s, done.
  Total 1 (delta 0), reused 0 (delta 0), pack-reused 0
  To http://coding.yundingshuyuan.com/DX_Lin/HelloGit.git
   * [new tag]         v0.1 -> v0.1
  ```

#### 删除标签

- `git tag -d <tagname>`

  应用到实例中：

  ```shell
  $ git tag -d v0.1
  Deleted tag 'v0.1' (was a3d5d86)
  ```

  上述命令并**不会**从任何远程仓库中移除这个标签，你必须用`git push <remote> :refs/tags/<tagname> `来更新你的远程仓库：

  ```shell
  $ git push hello :refs/tags/v0.1
  To http://coding.yundingshuyuan.com/DX_Lin/HelloGit.git
   - [deleted]         v0.1
  ```

  或者直接远程删掉它：

  ```shell
  $ git push <主机名> --delete <tag>
  ```



# 其它

## 注意事项

- 在 Windows 下使用 Git Bash 将文件添加到暂存区时，可能会有警告：

  ```shell
  warning: LF will be replaced by CRLF in <file>.
  ```

  这是因为 Windows 中的换行符为 CRLF，而 Linux 下的换行符为 LF，所以在执行 add 时出现提示。

  [解决方法](https://blog.csdn.net/wq6ylg08/article/details/88761581)

- 在 Windows 下首次连接远程仓库时会弹出窗口输入用户名和密码，这里的用户名和密码为代码托管平台的账户邮箱和密码。

## 本博客引用参考

[GitHub 官方文档](https://docs.github.com/cn/github/getting-started-with-github/set-up-git)

[Git 官方文档](https://git-scm.com/book/zh/v2/%E8%B5%B7%E6%AD%A5-%E5%85%B3%E4%BA%8E%E7%89%88%E6%9C%AC%E6%8E%A7%E5%88%B6)

[Git - 菜鸟教程](https://www.runoob.com/git/git-tutorial.html)

[廖雪峰的官方网站](https://www.liaoxuefeng.com/wiki/896043488029600)

> 本博客将不定期更新，欢迎提出不足与建议。