# 🍎 iPhone / iPad + Shadowrocket 使用教程

> iOS 平台 Shadowrocket（小火箭）基础配置指南。

---

## ⚠️ 先确认账号安全

> **❗ 重要**
> **设备「设置」中的 Apple ID 请使用你自己的账号。**
>
> 如果使用共享Apple ID下载 App，只在 App Store/媒体与购买项目中登录，不要把共享账号登录到 iCloud。

---

# 📥 第一步：下载客户端

Shadowrocket 等应用需要使用当前 App Store 支持该应用的地区账号。

👉 [🍎 App Store：Shadowrocket](https://apps.apple.com/us/app/shadowrocket/id932747118)

👉 [🇺🇸 美区 Apple Account 免费账号](appleid.md)

![App Store 示意](https://img.meituan.net/content/d6a2413a79d6303e2e3cd5e2b3f8a180271012.png)

---

# 🔐 第二步：获取服务节点

准备一个可用的 Shadowsocks / 订阅服务。

👉 [🔐 SS / SSR 订阅服务](ss.md)

---

# ⚡ 第三步：一键订阅

## 1. 登录订阅服务

使用 Safari 登录你的订阅服务，在个人中心找到：

**一键订阅 → 导入到 Shadowrocket**

系统会自动跳转到客户端。

![一键订阅](https://pic.ybfl.xyz/i/2023/02/22/10zhy4x-0.png)

---

## 2. 查看节点

回到客户端首页，可以看到已经导入的节点。

![节点列表](https://pic.ybfl.xyz/i/2023/02/22/11140tl-0.png)

---

## 3. 检查配置

进入配置页面。

普通用户优先保持默认配置。

![配置](https://pic.ybfl.xyz/i/2023/02/22/10zi0t8-0.png)

---

## 4. 开启自动更新

进入设置，将订阅更新相关选项按照客户端当前版本进行配置。

![订阅更新](https://pic.ybfl.xyz/i/2023/02/22/10zhv4u-0.png)

---

## 5. 选择路由模式

常见模式：

| 模式 | 作用 |
| :--- | :--- |
| 🎯 配置 | 按规则自动分流 |
| 🌐 代理 | 所有连接通过代理 |
| 🔗 直连 | 所有连接直连不经过代理 |
| 🧩 场景 | 根据你的网络环境切换 |

普通用户通常优先使用：

**配置**

![路由模式](https://pic.ybfl.xyz/i/2023/02/22/11140tl-0.png)

最后回到首页，开启连接开关。

---

# 🔗 第四步：手动添加订阅

如果不能一键导入，可以手动添加。

### 1. 复制订阅地址

在订阅服务中复制订阅 URL。

![复制订阅](https://pic.ybfl.xyz/i/2023/02/22/113lf8n-0.png)

### 2. 点击配置 → 右上角 `+`

![添加订阅](https://img.meituan.net/content/9d0aacc2e55eaa993f44e6df7bb3a92e62871.png)

### 3. 下载 `配置文件`

将订阅地址粘贴到 URL 点下载

![添加订阅](https://img.meituan.net/content/7b7086bbd1cad6ab037f2b6a238ed0e1121690.png)

### 4. 检查节点

![节点](https://pic.ybfl.xyz/i/2023/02/22/11140tl-0.png)

### 5. 测试节点

在开启代理后，点击连通性测试后面的【T】图标，改成勾选CONNECT，然后返回，点击【连通性测试】进行测试节点连通性

![节点测试](https://img.meituan.net/content/6b0bd36fb1c1463a59ed47c2c27254fb180159.png)
---

# 🛠️ 无法打开网页怎么办？

可以依次尝试：

1. 恢复客户端默认配置
2. 更换节点
3. 更换网络环境
4. 重启路由器
5. 更新订阅

---

## 🔐 再次提醒

- 不要把共享 Apple ID 登录到 iCloud
- 不要修改共享账号的密码、安全信息或付款信息
- 使用共享账号下载应用后及时退出
- 账号和应用的使用情况以 Apple 当前规则为准

