# 🖥 Windows + Clash 使用教程

> **推荐方案** · 适合 Windows 用户快速完成 Clash 配置。

---

## 🧭 教程流程

`下载客户端` → `导入订阅` → `选择节点` → `开启代理` → `测试网络`

---

## 📥 第一步：下载

Clash Verge 是 Windows 平台常见的 Clash 客户端。

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
<td align="center"><strong>Windows 下载</strong></td>
<td>

<a href="https://github.com/clash-verge-rev/clash-verge-rev/releases/download/v2.5.2/Clash.Verge_2.5.2_x64-setup.exe">
<img src="https://img.shields.io/badge/Setup-x64-2d7d9a?logo=windows">
</a>
<br>
<a href="https://github.com/clash-verge-rev/clash-verge-rev/releases/download/v2.5.2/Clash.Verge_2.5.2_x64_fixed_webview2-setup.exe">
<img src="https://img.shields.io/badge/Webview2-x64-67b7d1?logo=windows">
</a>

</td>
</tr>

<tr>
<td align="center"><strong>Windows 备用</strong></td>
<td>

<a href="https://gh-proxy.org/https://github.com/clash-verge-rev/clash-verge-rev/releases/download/v2.5.2/Clash.Verge_2.5.2_x64-setup.exe">
<img src="https://img.shields.io/badge/Setup-x64-2d7d9a?logo=windows">
</a>
<br>
<a href="https://gh-proxy.org/https://github.com/clash-verge-rev/clash-verge-rev/releases/download/v2.5.2/Clash.Verge_2.5.2_x64_fixed_webview2-setup.exe">
<img src="https://img.shields.io/badge/Webview2-x64-67b7d1?logo=windows">
</a>

</td>
</tr>

</tbody>
</table>

> **⚠️ 注意**
> 如果 Windows 防火墙或安全软件弹出提示，请先确认文件来源，再决定是否允许程序运行。

---

## ▶️ 第二步：运行程序

安装成功后运行：**Clash Verge**

![Clash 启动界面](https://img.meituan.net/content/0f42cca897aa102a3b176cad1e4a9ff172897.png)

---

## 🔗 第三步：导入订阅

点击左侧：**订阅** 把复制的订阅地址粘贴到 **订阅栏**，点击 **导入**。



![配置页面](https://img.meituan.net/content/098268c6f3c5bb75603fd0e1f67f4b6a82922.png)

---

## 🌐 第四步：选择节点和模式

点击左侧：**代理** 

等待自动测试后自行选择节点。

![代理页面](https://img.meituan.net/content/50335aee65fe8acbc765d0fd4d03960b142104.png)

常见模式：

| 模式 | 作用 |
| :--- | :--- |
| 🎯 **规则** | 根据规则自动分流 |
| 🌐 **全局** | 所有流量通过代理 |
| 🔗 **直连** | 所有流量直接连接 |
| 🧩 **脚本** | 高级用户使用 |

> **💡 提示**
> 普通用户优先使用 **规则（Rule）** 模式，具体效果取决于当前配置文件。

---

## ⚡ 第五步：开启代理

切换到 **设置** 把 **系统代理**、**DNS覆写**、**IPV6**、**统一延迟** 按钮打开，开始使用。

![开启系统代理](https://img.meituan.net/content/0dc64426fdc1154f161c412b22c49395106247.png)

---

## 🧩 虚拟网卡模式

Clash Verge默认主要影响系统代理支持的流量。

如果需要让更多 Windows 应用接入代理，可以根据客户端版本研究 **虚拟网卡模式**。

> **ℹ️ 说明**
> 不同 Clash 分支的界面和功能可能不同，请以你当前安装的客户端版本为准。

---

## 🛠️ 订阅无法直接更新

如果客户端无法直接更新订阅，可以：

1. 复制订阅链接
2. 在浏览器中打开
3. 复制返回的完整文本
4. 保存为文本文件
5. 根据客户端要求保存为 YAML 配置
6. 在「配置」页面导入

