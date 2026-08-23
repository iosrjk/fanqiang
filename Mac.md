# 💻 macOS + Clash Verge 使用教程

> macOS 平台 Clash 基础配置指南。

---

## 🧭 教程流程

`下载` → `运行` → `导入订阅` → `选择节点` → `开启代理`

---

## 📥 第一步：下载

下载地址：

<table>
<thead>
<tr>
<th>OS</th>
<th>Download</th>
</tr>
</thead>

<tbody>

<tr>
<td align="center"><strong>macOS 下载</strong></td>
<td>

<a href="https://github.com/clash-verge-rev/clash-verge-rev/releases/download/v2.5.2/Clash.Verge_2.5.2_aarch64.dmg">
<img src="https://img.shields.io/badge/DMG-Apple%20Silicon-000000?logo=apple">
</a>
<br>
<a href="https://github.com/clash-verge-rev/clash-verge-rev/releases/download/v2.5.2/Clash.Verge_2.5.2_x64.dmg">
<img src="https://img.shields.io/badge/DMG-Intel%20x64-00A9E0?logo=apple">
</a>

</td>
</tr>

<tr>
<td align="center"><strong>macOS 备用</strong></td>
<td>

<a href="https://gh-proxy.org/https://github.com/clash-verge-rev/clash-verge-rev/releases/download/v2.5.2/Clash.Verge_2.5.2_aarch64.dmg">
<img src="https://img.shields.io/badge/DMG-Apple%20Silicon-000000?logo=apple">
</a>
<br>
<a href="https://gh-proxy.org/https://github.com/clash-verge-rev/clash-verge-rev/releases/download/v2.5.2/Clash.Verge_2.5.2_x64.dmg">
<img src="https://img.shields.io/badge/DMG-Intel%20x64-00A9E0?logo=apple">
</a>

</td>
</tr>

</tbody>
</table>

下载后解压到任意目录。

> **⚠️ 注意**
> 原文部分描述使用了 Windows 软件名称。如果你是在 macOS 上操作，请确认下载的客户端确实支持 macOS，再运行。

---

## ▶️ 第二步：运行客户端

下载后运行下载的【Clash.Verge.dmg】进入如下界面

![客户端界面1](https://img.meituan.net/content/e4425de749f3459161a8652a16523fd0513082.gif)

![客户端界面2](https://img.meituan.net/content/93af792fea94d9406bb0fffe15aecfc790384.png)

---

## 🔗 第三步：导入订阅

进入你的订阅服务，在：

**我的订阅 / 仪表盘**

找到并点击复制订阅地址。

![仪表盘](https://img.meituan.net/content/051df8eb2c91915dfc1bfa8bd91e955e80658.png)

在客户端中点击：**订阅**

粘贴订阅链接并导入。

![导入配置](https://img.meituan.net/content/2de94f842b1c9e8065fd29b9fcf3362088974.png)

---

## 🌐 第四步：选择节点和模式

进入：**代理**

选择需要使用的节点和代理模式。

![代理](https://img.meituan.net/content/2fcc6a6f14edb2493112b17298ae347e323126.png)

然后切换到：**设置**

把「系统代理」「IPV6」「统一延迟」按钮打开，开始使用。。

![设置](https://img.meituan.net/content/961cb08ec2216cac4a326a062a352201329376.png)

---
## ❗ 节点超时（Timeout）处理方法

切换到：**设置**

把「DNS覆写」打开，即可恢复。返回到「代理」栏，点击「wifi」图标刷新延迟。

![dns设置](https://img.meituan.net/content/1052903d0fbf79f0be3ccdd08e17800e294394.png)

![刷新](https://img.meituan.net/content/9efe63afe35c251208864e91db2d12e9323452.png)

---

## 🧩 TUN 模式

如果需要让更多 macOS 应用接入代理，可以研究当前客户端支持的 TUN 功能。

> **ℹ️ 说明**
> TUN、系统代理以及规则模式的实际行为与客户端版本和配置文件有关，请以当前版本说明为准。

---

## 🛠️ 订阅无法更新

如果客户端无法直接更新订阅：

1. 复制订阅地址
2. 在浏览器打开
3. 复制返回内容
4. 保存为文本文件
5. 根据客户端要求保存为 YAML
6. 导入配置页面

