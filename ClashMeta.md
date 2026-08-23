# 🤖 Android + Clash Meta 使用教程

> Clash Meta Android 基础配置指南。

---

## ✨ 客户端简介

Clash 是基于规则的网络代理核心，Clash Meta Android 是 Android 平台上的客户端。

常见能力包括：

- 🔄 切换代理模式和节点
- 📡 节点延迟测试
- 🔗 URL 订阅配置
- 📊 规则命中分析
- 📝 日志输出

常见协议支持取决于具体客户端版本。

---

## 🧰 准备工作

开始前准备：

- Android 7.0+
- Clash Meta Android 客户端
- 有效的代理订阅

下载入口：
<table>
<thead>
<tr>
<th>OS</th>
<th>Download</th>
</tr>
</thead>

<tbody>

<tr>
<td align="center"><strong>Android 下载</strong></td>
<td>

<a href="https://github.com/MetaCubeX/ClashMetaForAndroid/releases/download/v2.11.33/cmfa-2.11.33-meta-arm64-v8a-release.apk">
<img src="https://img.shields.io/badge/APK-ARMv8-168039?logo=android">
</a>
<br>
<a href="https://github.com/MetaCubeX/ClashMetaForAndroid/releases/download/v2.11.33/cmfa-2.11.33-meta-armeabi-v7a-release.apk">
<img src="https://img.shields.io/badge/APK-ARMv7-45bf55?logo=android">
</a>
<br>
<a href="https://github.com/MetaCubeX/ClashMetaForAndroid/releases/download/v2.11.33/cmfa-2.11.33-meta-universal-release.apk">
<img src="https://img.shields.io/badge/APK-x64-96ed89?logo=android">
</a>

</td>
</tr>

<tr>
<td align="center"><strong>Android 备用</strong></td>
<td>

<a href="https://gh-proxy.org/https://github.com/MetaCubeX/ClashMetaForAndroid/releases/download/v2.11.33/cmfa-2.11.33-meta-arm64-v8a-release.apk">
<img src="https://img.shields.io/badge/APK-ARMv8-168039?logo=android">
</a>
<br>
<a href="https://gh-proxy.org/https://github.com/MetaCubeX/ClashMetaForAndroid/releases/download/v2.11.33/cmfa-2.11.33-meta-armeabi-v7a-release.apk">
<img src="https://img.shields.io/badge/APK-ARMv7-45bf55?logo=android">
</a>
<br>
<a href="https://gh-proxy.org/https://github.com/MetaCubeX/ClashMetaForAndroid/releases/download/v2.11.33/cmfa-2.11.33-meta-universal-release.apk">
<img src="https://img.shields.io/badge/APK-x64-96ed89?logo=android">
</a>

</td>
</tr>

</tbody>
</table>

👉 [🔐 获取节点 / 订阅](ss.md)

---

# 🔗 方法一：URL 订阅

## 1. 获取订阅地址

登录你购买的机场，在个人中心找到订阅地址并复制。

---

## 2. 打开「配置」

进入 Clash Meta：

**配置 → 点击+号 → 从 URL 导入 → 填入URL → 保存**

![配置页面](https://img.meituan.net/content/9c19dec5ab2de509975d0c0fa53c45fe101965.png)

---

## 3. 粘贴订阅地址

输入订阅 URL 并保存。（自动更新可填也可不填）

![导入 URL](https://img.meituan.net/content/672f77e484edcd2d38368263c9c71880120269.png)

---

## 4. 选中订阅

选择刚刚添加的配置。

![选择配置](https://img.meituan.net/content/7c96cfcd843da553947f8f6b246e82bb62067.png)

---

## 5. 开启 VPN

返回首页，打开开关。

第一次使用系统会询问是否允许创建 VPN 连接，按照系统提示允许即可。

![开启代理](https://img.meituan.net/content/7a638f5d804ad4c9a16de305d4fc48d2187191.png)

---

## 6. 切换节点

进入：

**代理**

在策略组中选择需要使用的节点。

![切换节点](https://img.meituan.net/content/651c8bb3dc601e5a200a434b7b7deaa3165039.png)

点击节点即可切换。

---

## ⚡ 7. 测试延迟

点击延迟测试图标，可以查看节点响应时间。

![测试节点](https://img.meituan.net/content/86ee53c3a57dd9dfdcd01b22b3089caa120346.png)

> **💡 提示**
> 延迟只是网络响应指标，不等于实际网页访问速度。实际效果还会受到线路、拥塞和目标网站影响。

---

# 📁 方法二：本地文件导入

进入：

**配置 → 新配置 → 从文件导入**

选择本地配置文件。

![本地导入](https://img.meituan.net/content/5f99a13f9234e1b53e36623ac3051e5a84239.png)

---


# 📱 DNS覆写

进入：

**设置 → 覆写 → DNS → 策略**

选择【使用内置】

![DNS覆写](https://img.meituan.net/content/0b9909606ecc21b707c2cf700cb9f7d7116201.png)

---

# 🌐 代理模式

| 模式 | 作用 |
| :--- | :--- |
| 🌍 Global | 所有请求通过代理 |
| 🎯 Rule | 根据规则自动分流 |
| 🔗 Direct | 所有请求直连 |
| 🧩 PAC | 根据 PAC 文件判断 |

> **💡 提示**
> 普通用户通常优先使用 **Rule / 规则模式**，实际行为以配置文件为准。

---

# 🛠️ 常见订阅错误

### `Invalid Config: yaml: unmarshal errors`

如果看到类似：

```text
Invalid Config:yaml:unmarshal errors:
line 1:cannot unmarshal !!str ...
```

通常表示当前 URL 不是 Clash 所需格式，或者复制了错误类型的订阅链接。

---

### `Proxy is invalid: Unexpected null or empty`

如果出现：

```text
Invalid Config:Value for 'Proxy' is invalid:
Unexpected null or empty
```

检查：

- 订阅是否为空
- 套餐是否有效
- 订阅是否过期
- 配置文件格式是否正确

