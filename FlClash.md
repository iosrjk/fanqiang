# 🤖 Android + FlClash 使用教程

> Android 用户的 FlClash 基础配置指南。

---

## ✨ 客户端简介

FlClash 是一款简洁、开源、跨平台的 Clash 代理客户端，帮助用户轻松管理代理节点和网络规则。

常见能力包括：

- 🔄 切换代理模式和节点
- 📡 节点延迟测试
- 🔗 URL 订阅配置
- 📊 规则分流
- 📝 日志输出

常见协议支持取决于具体客户端版本。

---

## 📥 第一步：下载 FlClash

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

<a href="https://github.com/chen08209/FlClash/releases/download/v0.8.96/FlClash-0.8.96-android-arm64-v8a.apk">
<img src="https://img.shields.io/badge/APK-ARMv8-168039?logo=android">
</a>
<br>
<a href="https://github.com/chen08209/FlClash/releases/download/v0.8.96/FlClash-0.8.96-android-armeabi-v7a.apk">
<img src="https://img.shields.io/badge/APK-ARMv7-45bf55?logo=android">
</a>
<br>
<a href="https://github.com/chen08209/FlClash/releases/download/v0.8.96/FlClash-0.8.96-android-x86_64.apk">
<img src="https://img.shields.io/badge/APK-x64-96ed89?logo=android">
</a>

</td>
</tr>

<tr>
<td align="center"><strong>Android 备用</strong></td>
<td>

<a href="https://gh-proxy.org/https://github.com/chen08209/FlClash/releases/download/v0.8.96/FlClash-0.8.96-android-arm64-v8a.apk">
<img src="https://img.shields.io/badge/APK-ARMv8-168039?logo=android">
</a>
<br>
<a href="https://gh-proxy.org/https://github.com/chen08209/FlClash/releases/download/v0.8.96/FlClash-0.8.96-android-armeabi-v7a.apk">
<img src="https://img.shields.io/badge/APK-ARMv7-45bf55?logo=android">
</a>
<br>
<a href="https://gh-proxy.org/https://github.com/chen08209/FlClash/releases/download/v0.8.96/FlClash-0.8.96-android-x86_64.apk">
<img src="https://img.shields.io/badge/APK-x64-96ed89?logo=android">
</a>

</td>
</tr>

</tbody>
</table>


🗂️ [网盘版本](https://pan.quark.cn/s/c5a3a0e3fefc)

> **ℹ️ 说明**
> 下载第三方 APK 前，请自行确认文件来源和安全性。

---

## 🔐 第二步：获取节点

前往：👉 [🔐 SS / SSR 节点服务](ss.md)

准备好可用订阅信息。

---

## 📷 第三步：导入订阅

进入 FlClash：**配置 → 添加配置 → 通过 URL 获取配置文件 → 填入URL → 提交**

![FlClash 配置示意](https://img.meituan.net/content/f170d24c0ad8d95ad7a7b72458c80abc138025.png)


---


## ⚡ 第四步：测试节点

点击 **代理** 然后点击 **延迟测试** 刷新节点延迟后，自行选择节点。

![FlClash 测试节点](https://img.meituan.net/content/26c941ea6b21c2a70c8a35ce160665ca82955.png)

---

## 🌐 第五步：开启代理

点击 **仪表盘**，然后点击 **开启** 按钮。

![FlClash 开启代理](https://img.meituan.net/content/2cea6792a0aa56894695e86c04bdcf6995326.png)

首次连接FlClash提示 **网络连接请求**，点 **确定** 开始使用。

![FlClash 开启代理2](https://img.meituan.net/content/2a7027af54c18b835c0853bf56dc547c85529.png)

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

