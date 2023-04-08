const CACHE_NAME = "avatars";

const colors = [
  "#00AA55",
  "#009FD4",
  "#B381B3",
  "#939393",
  "#E3BC00",
  "#D47500",
  "#DC2A2A",
];

const nameToColor = (name) => {
  const colorIndex =
    name
      .split("")
      .map((i) => i.charCodeAt(0))
      .reduce((a, b) => a + b, 0) % colors.length;
  return colors[colorIndex].substring(1);
};

export const cacheAvatar = async (name) => {
  const cache = await caches.open(CACHE_NAME);
  const color = nameToColor(name);
  const url = `https://ui-avatars.com/api/?name=${name}&background=${color}`;

  try {
    cache.add(url);
  } catch (e) {
    console.log(e);
  }
};

export const getAvatar = async (name) => {
  const cache = await caches.open(CACHE_NAME);
  const color = nameToColor(name);
  const url = `https://ui-avatars.com/api/?name=${name}&background=${color}`;

  const avatar = await cache.match(url);
  const avatarImage = URL.createObjectURL(await avatar.blob());

  if (!avatar) {
    cacheAvatar(name);
    return $(`<img src=${url} />`);
  }

  return $(`<img src="${avatarImage}"/>`);
};
