// v0.1 MEASUREMENT GAUGES ONLY. No cup holder body is modeled yet.
// Reference: OEM Volvo VNL cup holder 84752175 REV P02 (PC/ABS), photos
// IMG_0149..0161 taken 2026-09-29. Photo tape readings are approximate.
// Dimensions in mm. Print at 100%. See README.md.
part="bottle_ring"; // bottle_ring | cup_step_gauge
$fn=128;
// Yeti bottle (owner's) base read as ~3.6 in (~91.4 mm) from IMG_0161; not a caliper value.
ring_id=93.5;      // exported at 92.0, 93.5 and 95.0
ring_h=20;
ring_wall=2.4;
tab_w=28;
tab_l=14;
tab_t=2;
// Stepped plug for the OEM cup bore: widest step on the bed, narrow end goes
// into the cup. The step that rests on the cup wall gives the bore diameter there.
step_max=104;      // OEM rim read as ~4.0 in (~101 mm) from IMG_0159
step_min=74;
step_d=3;          // diameter change per step (1.5 mm ledge)
step_h=5;
shell=2;
steps=floor((step_max-step_min)/step_d)+1;
assert(ring_id+2*ring_wall+2*tab_l+20<=220,"Ring exceeds bed");
assert(step_max+20<=220,"Step gauge exceeds bed");

module label(s,size=5){
 text(s,size=size,font="DejaVu Sans:style=Bold",halign="center",valign="center");
}
module bottle_ring(){
 od=ring_id+2*ring_wall;
 difference(){
  union(){
   cylinder(d=od,h=ring_h);
   // Flat tab at the base with the inside diameter engraved.
   translate([od/2-ring_wall,-tab_w/2,0]) cube([tab_l+ring_wall,tab_w,tab_t]);
  }
  translate([0,0,-1]) cylinder(d=ring_id,h=ring_h+2);
  translate([od/2+tab_l/2,0,tab_t-0.6]) linear_extrude(1) rotate(90) label(str(ring_id),4);
 }
}
module cup_step_gauge(){
 difference(){
  union() for(i=[0:steps-1])
   translate([0,0,i*step_h]) cylinder(d=step_max-i*step_d,h=step_h+(i<steps-1?0.01:0));
  // Stepped hollow keeps a `shell` wall on every step; the 1.5 mm inner
  // ledges are short overhangs that print without support.
  for(i=[0:steps-1])
   translate([0,0,i==0?-1:i*step_h-0.01]) cylinder(d=step_max-i*step_d-2*shell,h=step_h+(i==0?1.01:0.02)+(i==steps-1?1:0));
  // Index notch on the widest step marks step 0; count steps upward from it.
  translate([step_max/2-1.5,-1,-1]) cube([3,2,step_h+1]);
 }
}
if(part=="bottle_ring") bottle_ring();
else if(part=="cup_step_gauge") cup_step_gauge();
else assert(false,str("Unknown part: ",part));
