<template>
  <main>
    <n-card hoverable>
      <n-space>
        <div class="text">当前时间：</div>
        <div class="text" style="color: green">{{ currentTime }}</div>
      </n-space>
      <n-space>
        <div class="text">当前时刻：</div>
        <div class="text" style="color: green">{{ currentContent }}</div>
      </n-space>
      <n-space>
        <div class="text">距离刷新：</div>
        <div class="text" style="color: orange">{{ diffInMinutes }}</div>
      </n-space>
      <n-space>
        <div class="text">下一时刻：</div>
        <div class="text" style="color: orange">{{ nextContent }}</div>
      </n-space>
    </n-card>
    <n-card hoverable>
      <div class="container">
        <div class="box north">北{{ points.北 }}</div>
        <div class="box south">南{{ points.南 }}</div>
        <div class="box east">东{{ points.东 }}</div>
        <div class="box west">西{{ points.西 }}</div>
        <div class="box southeast">石碑</div>
      </div>
    </n-card>
    <div class="copyright">
      上星@唯我独尊
    </div>
  </main>
</template>
<script setup>
import { ref } from "vue";
import { DateTime } from "luxon";

const currentTime = ref();
const currentContent = ref("");
const diffInMinutes = ref("");
const nextTime = ref("");
const nextContent = ref("");
const matches = ref("");
const points = ref({});
const getCurrentTime = () => {
  const currentTime = DateTime.now()
    .setZone("Asia/Shanghai")
    .toFormat("HH:mm:ss");
  return currentTime;
};
const getNextTime = () => {
  // 获取当前时间
  const now = DateTime.now().setZone("Asia/Shanghai");

  // 计算当前时间的分钟数距离最近的15分钟间隔
  const minutes = now.minute;
  const remainder = 15 - (minutes % 15);
  const nextQuarter = now
    .plus({ minutes: remainder, seconds: -now.second })
    .toFormat("HH:mm:ss");
  return nextQuarter;
};

function getTimeToNextQuarter() {
  // 获取当前时间
  const now = DateTime.local();

  // 计算当前时间的分钟数距离最近的15分钟间隔
  const minutes = now.minute;
  const remainder = 15 - (minutes % 15);
  const nextQuarter = now.plus({ minutes: remainder, seconds: -now.second });

  // 计算当前时间到下一个 15 分钟的时间差
  const diff = nextQuarter.diff(now, ["minutes", "seconds"]).toObject();

  // 格式化返回“xx分钟xx秒”的字符串
  return `${Math.floor(diff.minutes)}分钟${Math.floor(diff.seconds)}秒`;
}

const getDirectionString = (currentTime) => {
  const hour = currentTime.split(":")[0];
  // 时间段数组
  const timeSegments = [
    { hour: 0, value: "东 9 | 南 0 | 西 1 | " },
    { hour: 5, value: "南 0 | 西 1 | 北 4 | " },
    { hour: 11, value: "东 9 | 西 1 | 北 4 | " },
    { hour: 17, value: "东 9 | 南 0 | 北 4 | " },
    { hour: 23, value: "东 9 | 南 0 | 西 1 | " },
  ];

  // 查找匹配的时间段字符串
  const segmentValue =
    timeSegments.reverse().find((segment) => hour >= segment.hour)?.value || "";

  // D列和E列的时间 方向数据
  const timeToDirection = {
    "00:00:00": "北 9",
    "00:15:00": "北 0",
    "00:30:00": "北 1",
    "00:45:00": "北 2",
    "01:00:00": "北 3",
    "01:15:00": "北 4",
    "01:30:00": "北 4",
    "01:45:00": "北 4",
    "02:00:00": "北 4",
    "02:15:00": "北 4",
    "02:30:00": "北 4",
    "02:45:00": "北 4",
    "03:00:00": "北 3",
    "03:15:00": "北 2",
    "03:30:00": "北 1",
    "03:45:00": "北 0",
    "04:00:00": "北 9",
    "04:15:00": "北 8",
    "04:30:00": "北 7",
    "04:45:00": "北 6",
    "05:00:00": "东 0",
    "05:15:00": "东 1",
    "05:30:00": "东 2",
    "05:45:00": "东 3",
    "06:00:00": "东 4",
    "06:15:00": "东 5",
    "06:30:00": "东 6",
    "06:45:00": "东 7",
    "07:00:00": "东 8",
    "07:15:00": "东 9",
    "07:30:00": "东 9",
    "07:45:00": "东 9",
    "08:00:00": "东 9",
    "08:15:00": "东 9",
    "08:30:00": "东 9",
    "08:45:00": "东 9",
    "09:00:00": "东 8",
    "09:15:00": "东 7",
    "09:30:00": "东 6",
    "09:45:00": "东 5",
    "10:00:00": "东 4",
    "10:15:00": "东 3",
    "10:30:00": "东 2",
    "10:45:00": "东 1",
    "11:00:00": "南 1",
    "11:15:00": "南 2",
    "11:30:00": "南 3",
    "11:45:00": "南 4",
    "12:00:00": "南 5",
    "12:15:00": "南 6",
    "12:30:00": "南 7",
    "12:45:00": "南 8",
    "13:00:00": "南 0",
    "13:15:00": "南 0",
    "13:30:00": "南 0",
    "13:45:00": "南 0",
    "14:00:00": "南 0",
    "14:15:00": "南 0",
    "14:30:00": "南 0",
    "14:45:00": "南 0",
    "15:00:00": "南 9",
    "15:15:00": "南 8",
    "15:30:00": "南 7",
    "15:45:00": "南 6",
    "16:00:00": "南 5",
    "16:15:00": "南 4",
    "16:30:00": "南 3",
    "16:45:00": "南 2",
    "17:00:00": "西 2",
    "17:15:00": "西 3",
    "17:30:00": "西 4",
    "17:45:00": "西 5",
    "18:00:00": "西 6",
    "18:15:00": "西 7",
    "18:30:00": "西 8",
    "18:45:00": "西 9",
    "19:00:00": "西 1",
    "19:15:00": "西 1",
    "19:30:00": "西 1",
    "19:45:00": "西 1",
    "20:00:00": "西 1",
    "20:15:00": "西 1",
    "20:30:00": "西 1",
    "20:45:00": "西 1",
    "21:00:00": "西 0",
    "21:15:00": "西 9",
    "21:30:00": "西 8",
    "21:45:00": "西 7",
    "22:00:00": "西 6",
    "22:15:00": "西 5",
    "22:30:00": "西 4",
    "22:45:00": "西 3",
    "23:00:00": "北 5",
    "23:15:00": "北 6",
    "23:30:00": "北 7",
    "23:45:00": "北 8",
  };

  // 按时间顺序查找 direction
  const directionKeys = Object.keys(timeToDirection).sort();
  let direction = "";
  for (let i = 0; i < directionKeys.length; i++) {
    if (currentTime >= directionKeys[i]) {
      direction = timeToDirection[directionKeys[i]];
    } else {
      break;
    }
  }
  return `${segmentValue}${direction}`;
};
setInterval(() => {
  currentTime.value = getCurrentTime();
  nextTime.value = getNextTime();
  currentContent.value = getDirectionString(currentTime.value);
  nextContent.value = getDirectionString(nextTime.value);
  diffInMinutes.value = getTimeToNextQuarter();
  matches.value = currentContent.value.split(" | ");
  matches.value.forEach((match) => {
    const [, direction, point] = match.match(/(东|西|北|南) (\d+)/);
    points.value[direction] = parseInt(point, 10);
  });
}, 1000);
</script>

<style scoped>
.text {
  font-size: 18px;
  font-weight: bold;
}
.container {
  position: relative;
  width: 300px;
  height: 300px;
  border: 1px solid #000;
  display: flex;
  justify-content: center;
  align-items: center;
}

.box {
  position: absolute;
  padding: 10px;
  color: white;
  font-weight: bold;
  background-color: #007acc;
  border-radius: 5px;
}

.north {
  top: 0;
  left: 20%;
  transform: translateY(-50%);
}

.south {
  bottom: 0;
  right: 20%;
  transform: translateY(50%);
}

.east {
  right: 0;
  top:20%;
  transform: translateX(50%);
}

.west {
  left: 0;
  bottom: 20%;
  transform: translateX(-50%);
}
.southeast {
  bottom: 0;
  right: 0;
  transform: translate(50%, 50%);
  background-color: #555; /* 为“石碑”添加不同的背景颜色 */
}
.copyright{
  position: absolute;
  bottom: 0;
  left: 0;
  font-size: 12px;
  color: #999;
}
</style>
