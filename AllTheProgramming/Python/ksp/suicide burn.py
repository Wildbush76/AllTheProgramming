import krpc
import time
import math
conn = krpc.connect()
vessel = conn.space_center.active_vessel
print("starting")
S_altitude = conn.add_stream(getattr, vessel.flight(), 'surface_altitude')
altitude = conn.add_stream(getattr, vessel.flight(), 'mean_altitude')
thrust = conn.add_stream(getattr, vessel, 'thrust')
mass = conn.add_stream(getattr, vessel, 'mass')
speed = conn.add_stream(getattr,vessel.flight(vessel.orbit.body.reference_frame), 'speed')
running = True
acceleration = 0
vessel.sas = True
vessel.rcs = True

throttle = 0.1
print("doing it")
maxThrust = sum(e.available_thrust for e in vessel.parts.engines if e.active and e.has_fuel)
stage = 0
while running:
    if stage == 1:
        acceleration = ((speed()**2)/(S_altitude() - 5))/2
        g = ((6.67259 * 10**-11) * (vessel.orbit.body.mass))/((altitude()+vessel.orbit.body.equatorial_radius)**2)
        
        thrustNeeded = (g + acceleration)*mass()
        throttle = (throttle/thrust())*thrustNeeded
        vessel.control.throttle = throttle
        
        if S_altitude() < 4 or speed() < 2:
            print("landed, engine shutdown")
            vessel.control.throttle = 0
            break
        elif S_altitude() < 200 and vessel.control.gear == False:
            vessel.control.gear = True
        time.sleep(0.1)
        
    elif stage == 0:
        Acc = (maxThrust/mass())
        if 80000 > S_altitude() > 15000:
            vessel.control.brakes = True
        elif vessel.control.brakes == True:
            vessel.control.brakes = False
        if S_altitude() <= ((speed()**2)/Acc) and S_altitude() < 10000:
            stage = 1
            print("landing burn begin")
            vessel.control.sas_mode = conn.space_center.SASMode.retrograde
            vessel.control.throttle = throttle
            time.sleep(0.2)
            maxThrust = sum(e.available_thrust for e in vessel.parts.engines if e.active and e.has_fuel)
            continue
        time.sleep(0.5)
            
