// v0.2 MOUNT TEST ONLY: split snap posts for the holes under the dash ledge.
// Owner caliper values (2026-09-29): ledge hole 11.5 mm, post/hole spacing
// 75.5 mm center to center, ledge 20 mm thick; stock post 10 mm tall (2026-09-30).
// Dimensions in mm. Print at 100%, plate flat on the bed, posts up, no supports.
part="pitch_strip"; // pitch_strip | post_fit
$fn=64;
hole_d=11.5;       // measured
post_pitch=75.5;   // measured, center to center
post_h=10;         // measured: stock post height above the flange
shank_clear=0.4;   // shank is this much smaller than the hole
lead_d=9.5;        // tip diameter, for an easy start into the hole
barb_h=3;          // straight band of the barb
barb_from_top=2;   // top of the barb band below the tip
taper_h=2;         // barb back-taper down to the shank
slot_w=2.2;        // cross slot that lets the two halves squeeze together
slot_depth=8;      // slot length from the tip down
plate_t=3;
fit_barbs=[11.8,12.2,12.6]; // post_fit coupon: interference trial sizes
strip_barb=12.2;             // pitch_strip uses the middle size until one is chosen
shank_d=hole_d-shank_clear;
assert(slot_depth<post_h-1,"Slot would cut through the post base");
assert(max(fit_barbs)<hole_d+2,"Barb too large to push in");

module label(s,size=4){
 text(s,size=size,font="DejaVu Sans:style=Bold",halign="center",valign="center");
}
// Revolved post profile: shank, back-taper, barb band, lead-in cone to the tip.
module post(barb_d){
 zb=post_h-barb_from_top;          // top of barb band
 difference(){
  rotate_extrude() polygon([
   [0,-0.01],[shank_d/2,-0.01],
   [shank_d/2,zb-barb_h-taper_h],
   [barb_d/2,zb-barb_h],
   [barb_d/2,zb],
   [lead_d/2,post_h],
   [0,post_h]]);
  translate([-barb_d,-slot_w/2,post_h-slot_depth]) cube([2*barb_d,slot_w,slot_depth+1]);
 }
 // Base fillet ring so the post doesn't snap off at the plate.
 rotate_extrude() difference(){
  translate([shank_d/2-0.01,0]) square(1.5);
  translate([shank_d/2+1.5,1.5]) circle(r=1.5);
 }
}
module plate(w,d){
 hull() for(x=[3,w-3],y=[3,d-3]) translate([x,y]) cylinder(r=3,h=plate_t);
}
// Two posts at the measured spacing: checks pitch, seating and pull-out together.
module pitch_strip(){
 w=post_pitch+30; d=24;
 difference(){
  plate(w,d);
  translate([w/2,d/2,plate_t-0.6]) linear_extrude(1) label(str(post_pitch),4);
 }
 for(x=[15,15+post_pitch]) translate([x,d/2,plate_t-0.01]) post(strip_barb);
}
// Three single posts with different barb sizes: pick the one that snaps and holds.
module post_fit(){
 n=len(fit_barbs); gap=22; w=gap*n+6; d=30;
 difference(){
  plate(w,d);
  for(i=[0:n-1]) translate([gap/2+3+i*gap,5,plate_t-0.6]) linear_extrude(1) label(str(fit_barbs[i]),3.2);
 }
 for(i=[0:n-1]) translate([gap/2+3+i*gap,d/2+3,plate_t-0.01]) post(fit_barbs[i]);
}
if(part=="pitch_strip") pitch_strip();
else if(part=="post_fit") post_fit();
else assert(false,str("Unknown part: ",part));
