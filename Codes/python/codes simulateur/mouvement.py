from robot_api import (
    setmotor_speed1,
    setmotor_speed2,
    setmotor_speed3,
    setmotor_speed4,
    get_ball_x,
    get_ball_y,
    get_robot_x,
    get_robot_y,
)

v_avancer = 70
v_reculer = 70
v_crabe_droit = 70
v_crabe_gauche = 70
v_rota_droite = 70
v_rota_gauche = 70


def set_all(fl, fr, rl, rr):  # applique a tous les moteurs la v
    setmotor_speed1(fl)
    setmotor_speed2(fr)
    setmotor_speed3(rl)
    setmotor_speed4(rr)


def stop():
    set_all(0, 0, 0, 0)


def avancer(v=v_avancer):
    set_all(v, v, v, v)


def reculer(v=v_reculer):
    set_all(-v, -v, -v, -v)


def crabe_droite(v=v_crabe_droit):
    set_all(-v, v, v, -v)


def crabe_gauche(v=v_crabe_gauche):
    set_all(v, -v, -v, v)


def rotation_droite(v=v_rota_droite):
    set_all(-v, v, -v, v)


def rotation_gauche(v=v_rota_gauche):
    set_all(v, -v, v, -v)


def step(dt, state):  # mettre ici le code a executer
    bx, by = get_ball_x(), get_ball_y()
    rx, ry = get_robot_x(), get_robot_y()

    cible_x, cible_y = bx - 0.18, by
    seuil = 0.015

    vx = -50 if abs(rx - cible_x) > seuil else 0
    vy = 50 if abs(ry - cible_y) > seuil else 0

    vx *= -1 if rx < cible_x else 1
    vy *= -1 if ry < cible_y else 1

    if vx == 0 and vy == 0:
        stop()
    else:
        set_all(vx + vy, vx - vy, vx - vy, vx + vy)