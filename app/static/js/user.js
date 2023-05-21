const CACHE_NAME = "avatars";

//avatar colors
const colors = [
  "#00AA55",
  "#009FD4",
  "#B381B3",
  "#939393",
  "#E3BC00",
  "#D47500",
  "#DC2A2A",
  "#77b164",
  "#db8ba3",
  "#9e57cd",
  "2aedc1",
];

//adding avatar color
const nameToColor = (name) => {
  const colorIndex =
    name
      .split("")
      .map((i) => i.charCodeAt(0))
      .reduce((a, b) => a + b, 0) % colors.length;
  return colors[colorIndex].substring(1);
};

//adding Avatar to cache
export const cacheAvatar = async (name) => {
  const cache = await caches.open(CACHE_NAME);
  const color = nameToColor(name);
  const url = `https://ui-avatars.com/api/?name=${name}&background=${color}&rounded=true`;

  cache.add(url);
};

//getting avatar from cache
export const getAvatar = async (name) => {
  const cache = await caches.open(CACHE_NAME);
  const color = nameToColor(name);
  const url = `https://ui-avatars.com/api/?name=${name}&background=${color}&rounded=true`;
  const avatar = await cache.match(url);

  if (!avatar) {
    cacheAvatar(name);
    return url;
  }
  const avatarImage = URL.createObjectURL(await avatar.blob());

  return avatarImage;
};
