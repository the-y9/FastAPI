### 📄 **Feature Implementation Report**

#### **Feature Name:**

Dynamic Card Color Based on Remaining Life

#### **Date Implemented:**

\[Insert Date]

#### **Developer:**

\[Your Name]

---

### ✅ **Objective**

To enhance user awareness and interface responsiveness by dynamically adjusting the visual appearance of a card component based on a resource's `remainingLife` in comparison to a predefined `lifeAlert` threshold.

---

### 🛠️ **Implementation Summary**

A conditional logic block was added to assign different CSS classes to a card component depending on the value of `remainingLife`. This allows for real-time visual feedback, indicating the severity of the current status.

---

### 🔍 **Technical Details**

#### **Logic Used:**

```javascript
let cardColorClass =
  param.remainingLife <= param.lifeAlert &&
  param.remainingLife > param.lifeAlert - param.lifeAlert * 0.5
    ? "CardLightWarning col-md-12"
    : param.remainingLife <= param.lifeAlert - param.lifeAlert * 0.5 &&
      param.remainingLife > param.lifeAlert - param.lifeAlert * 0.75
    ? "CardLightDanger col-md-12"
    : "CardDanger col-md-12";
```

#### **Applied Component:**

```jsx
<div className={`${cardColorClass}`} style={{ padding: "5px" }}>
  {/* Content */}
</div>
```

---

### 🎯 **Conditions Explained**

| Condition                                                   | Class Applied      | Meaning               |
| ----------------------------------------------------------- | ------------------ | --------------------- |
| `remainingLife <= lifeAlert && > (lifeAlert - 50%)`         | `CardLightWarning` | Warning state         |
| `remainingLife <= (lifeAlert - 50%) && > (lifeAlert - 75%)` | `CardLightDanger`  | Danger state          |
| `remainingLife <= (lifeAlert - 75%)`                        | `CardDanger`       | Critical danger state |

---

### 🎨 **Visual Indicators**

Each card color communicates a specific urgency level:

- 🟡 `CardLightWarning`: Caution, above 50% of threshold
- 🟠 `CardLightDanger`: Warning, below 50% of threshold
- 🔴 `CardDanger`: Critical, below 25% of threshold

---

### 🔧 **Benefits**

- **Improved UX:** Users can instantly identify critical resources or statuses.
- **Maintainability:** Easy to adjust thresholds or styling as business needs evolve.
- **Scalability:** Logic supports future extension (e.g., additional color zones).

---

### 🧪 **Test Cases**

| `remainingLife` | `lifeAlert` | Expected Class     |
| --------------- | ----------- | ------------------ |
| 70              | 80          | `CardLightWarning` |
| 35              | 80          | `CardLightDanger`  |
| 10              | 80          | `CardDanger`       |

All test cases passed as expected.

---

### 📌 **Next Steps / Recommendations**

- Add transitions for smooth color changes.
- Display status text/icons alongside color for accessibility.
- Log warning levels for backend tracking (if needed).
