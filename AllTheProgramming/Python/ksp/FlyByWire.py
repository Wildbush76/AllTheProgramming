import krpc
import time
print("ready")
time.sleep(1)
conn = krpc.connect()
vessel = conn.space_center.active_vessel
vessel.auto_pilot.target_pitch_and_heading(90,90)
vessel.auto_pilot.engage()
vessel.control.rcs = True
#vessel.control.activate_next_stage()

state = 1
target = 90
throttle = 1

while True:
    altitude = vessel.flight().surface_altitude
    speed = vessel.flight(vessel.orbit.body.reference_frame).speed
    Gs = vessel.flight().g_force
    
    if state == 1:
        if speed < 300 or altitude > 25000:
            throttle = 1
        else:
            if Gs > 1.8:
                throttle -= 0.01
            elif Gs < 1:
                throttle += 0.01
        if altitude < 25000:       
            target = 90 - (altitude/25000)*70
        else:
            target = 30
        vessel.auto_pilot.target_pitch_and_heading(target,90)
        vessel.control.throttle = throttle

        if vessel.orbit.apoapsis-600000 > 99000:
            state = 2
            vessel.control.throttle = 0
            vessel.auto_pilot.target_pitch_and_heading(0,90)
        if vessel.thrust == 0.0 and vessel.control.throttle > 0:
            time.sleep(0.2)
            if vessel.thrust == 0.0:
                vessel.control.activate_next_stage()
    if state == 2: 
        if vessel.orbit.time_to_apoapsis < 30:
            vessel.control.activate_next_stage()
            state = 3
            
    if state == 3:
        #do that funny stuff for orbit
        if vessel.orbit.apoapsis-600000 > 99500 and vessel.orbit.periapsis-600000 > 99000 or vessel.orbit.periapsis-600000 > 99000:
            vessel.control.throttle = 0
            print("DEORBIT")
            input()
            state = 4
        TA = vessel.orbit.time_to_apoapsis
        if TA < 10:
            vessel.control.throttle = (10 - TA)/10
            vessel.auto_pilot.target_pitch_and_heading(10,90)
        elif TA > 500:
            vessel.control.throttle = 1
            vessel.auto_pilot.target_pitch_and_heading(15,90)
    if state == 4:
        vessel.auto_pilot.disengage()
        vessel.control.sas = True
        time.sleep(0.5)
        vessel.control.sas_mode = conn.space_center.SASMode.retrograde
        time.sleep(2)
        while vessel.orbit.periapsis-600000 > 40000:
            vessel.control.throttle = 1
        vessel.control.throttle = 0
        time.sleep(1)
        vessel.control.activate_next_stage()
        state = 5
    if state == 5:
        if altitude < 10000:
            vessel.control.activate_next_stage()
            vessel.control.parachutes = True
        if altitude < 1000:
            vessel.control.gear = True
            break
        
        
            
vessel.auto_pilot.disengage()
print("done!")
    
