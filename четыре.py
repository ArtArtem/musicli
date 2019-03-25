import sys
import pygame
import os
import requests


class MapParams(object):
    def __init__(self):
        self.lat = 55.729738
        self.lon = 37.664777
        self.zoom = 15
        self.type = "map"
        self.search_result = None
        self.use_postal_code = False

    def ll(self):
        return ll(self.len, self.lat)

    def update(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_PAGEUP:
            if self.zoom < 17:
                self.zoom += 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_PAGEDOWN:
            if self.zoom > 0:
                self.zoom -= 1

    def change_type(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_g:
            if self.type == "sat,skl":
                self.type = "sat"
            elif self.type == "sat":
                self.type = "map"
            elif self.type == "map":
                self.type = "sat,skl"

def load_map(mp):
    map_request = "http://static-maps.yandex.ru/1.x/?ll={},{}&z={}&l={}".format(mp.lon, mp.lat, mp.zoom, mp.type)
    response = requests.get(map_request)
    if not response:
        print("Ошибка выполнения запроса")
        print(map_request)
        print("Http статус:"), response.status_code, "(", response.reason, ")"
        sys.exit(1)
    map_file = "map.png"
    try:
        with open(map_file, "wb") as file:
            file.write(response.content)
    except IOError as ex:
        print("Ошибка записи временного файла")
        sys.exit(2)
    return map_file


def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 450))
    mp = MapParams()
    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            break
        mp.change_type(event)
        mp.update(event)
        map_file = load_map(mp)
        screen.blit(pygame.image.load(map_file), (0, 0))
        pygame.display.flip()

    pygame.quit()
    os.remove(map_file)


if __name__ == "__main__":
    main()