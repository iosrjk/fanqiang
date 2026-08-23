# 🖥 Windows + V2rayN 使用教程

> **Windows 推荐客户端之一** · 适合使用订阅配置管理多个节点。

---

## 🧭 教程流程

`下载` → `运行` → `导入订阅` → `更新节点` → `测试延迟` → `选择节点` → `开启系统代理`

---

## 📥 第一步：下载

V2rayN 是 Windows 平台常见的客户端。

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

<a href="https://github.com/2dust/v2rayN/releases/download/7.24.8/v2rayN-windows-64.zip">
<img src="https://img.shields.io/badge/Portable-x64-2d7d9a?logo=windows">
</a>


</td>
</tr>

<tr>
<td align="center"><strong>Windows 备用</strong></td>
<td>

<a href="https://gh-proxy.org/https://github.com/2dust/v2rayN/releases/download/7.24.8/v2rayN-windows-64.zip">
<img src="https://img.shields.io/badge/Portable-x64-2d7d9a?logo=windows">
</a>

</td>
</tr>

</tbody>
</table>

**系统要求：Windows 10 及以上**

> **⚠️ 注意**
> 如果 Windows 防火墙或安全软件提示风险，请先确认下载来源和文件完整性，再决定是否允许程序运行。

---

## ▶️ 第二步：运行程序

解压后，以管理员身份运行：**V2rayN.exe**

![V2rayN 主界面](https://img.meituan.net/content/845b4a9a67e47e9b5828378f784f848486340.png)

---

## 🔗 第三步：导入订阅

### 1. 导入分享链接

复制你的订阅链接，然后进入：**配置文件 → 从剪贴板导入分享链接**

![导入分享链接](https://img.meituan.net/content/2fd5751491753318d4b8bad2de36f35d109203.png)

![导入结果](https://img.meituan.net/content/2021a1d1c0427077145586a2423a41c6104952.png)

### 2. 更新订阅

进入：**订阅分组 → 更新全部订阅**

![更新订阅](https://img.meituan.net/content/5b6c1ef9e37e723f2713f45ef774ea8196662.png)

### 3. 查看节点

更新完成后，节点列表中会出现多个服务器配置。

![节点列表](https://img.meituan.net/content/5c3d96507ba09879033d394c49ff8eb8312453.png)

---

## 📡 第四步：测试节点

点击节点列表，然后：

**Ctrl + A → 右键 → 测试配置文件真连接延迟（多选）**

![测试延迟](https://img.meituan.net/content/3403c68c7845d37b5c37960fa3b3adf6305450.png)

如果出现延迟数字，说明该节点完成了基本连通性测试。

![测试延迟结果](https://img.meituan.net/content/0b36f5cd8f6f893d10c6551425702ed8220071.png)

---

## ⭐ 第五步：选择节点

选择延迟正常的节点：**右键 → 设为活动**

![设为活动配置](https://img.meituan.net/content/f9148758daf61e3fe30dfbc927bd0608233220.png)

---

## ⚡ 第六步：开启代理

选择节点后，根据当前客户端界面启用：**自动配置系统代理**

![开启系统代理](https://img.meituan.net/content/9109f8ed4cf207308a042fd8abaa2d7f226877.png)

开启成功后可以到浏览器检测一下ip是否变化，或者打开Google页面

![开启代理成功](https://img.meituan.net/content/16f4fb22c5db31b3061ec58e6aa83fc4230934.png)

如果不想用了把代理改为：**清除系统代理**

---

## 🛠️ 常见问题

### 节点全部超时

建议依次：

1. 更新订阅
2. 更换节点
3. 检查系统时间
4. 检查网络
5. 确认订阅套餐仍然有效

### 开启代理后网页无法访问

可以尝试：

- 更换节点
- 切换代理模式
- 暂时关闭其他 VPN / 代理软件
- 重启 V2rayN

