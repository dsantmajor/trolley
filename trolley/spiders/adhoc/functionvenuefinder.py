from __future__ import unicode_literals

import urllib2

from bs4 import BeautifulSoup
 
links = """http://www.functionvenuefinder.com.au/view_venue/nar/archer_resort
http://www.functionvenuefinder.com.au/view_venue/nbg/boomerang_hotel
http://www.functionvenuefinder.com.au/view_venue/nch/castle_hill_tavern
http://www.functionvenuefinder.com.au/view_venue/nco/colyton_hotel
http://www.functionvenuefinder.com.au/view_venue/ncn/crows_nest_hotel
http://www.functionvenuefinder.com.au/view_venue/net/ettamogah_pub
http://www.functionvenuefinder.com.au/view_venue/ngr/greenhouse_tavern
http://www.functionvenuefinder.com.au/view_venue/nki/kirribilli_hotel
http://www.functionvenuefinder.com.au/view_venue/nmi/macquarie_inn
http://www.functionvenuefinder.com.au/view_venue/nns/narrabeen_sands_hotel
http://www.functionvenuefinder.com.au/view_venue/nnb/new_brighton_hotel
http://www.functionvenuefinder.com.au/view_venue/npa/parkway_hotel
http://www.functionvenuefinder.com.au/view_venue/npy/pymble_hotel
http://www.functionvenuefinder.com.au/view_venue/nsm/smithfield_tavern
http://www.functionvenuefinder.com.au/view_venue/nrn/the_ranch
http://www.functionvenuefinder.com.au/view_venue/nwb/woolloomooloo_bay_hotel
http://www.functionvenuefinder.com.au/view_venue/njt/jewells_tavern
http://www.functionvenuefinder.com.au/view_venue/nmh/mattara_hotel
http://www.functionvenuefinder.com.au/view_venue/qab/albany_creek_tavern
http://www.functionvenuefinder.com.au/view_venue/qai/albion_hotel
http://www.functionvenuefinder.com.au/view_venue/qaa/alderley_arms_hotel
http://www.functionvenuefinder.com.au/view_venue/qax/alexandra_headlands_hotel
http://www.functionvenuefinder.com.au/view_venue/qat/allenstown_hotel
http://www.functionvenuefinder.com.au/view_venue/qan/anglers_arms_hotel
http://www.functionvenuefinder.com.au/view_venue/qoz/australian_national_hotel
http://www.functionvenuefinder.com.au/view_venue/qbv/balaclava_hotel
http://www.functionvenuefinder.com.au/view_venue/qbe/belmont_tavern
http://www.functionvenuefinder.com.au/view_venue/qbw/benowa_tavern
http://www.functionvenuefinder.com.au/view_venue/qbc/breakfast_creek_hotel
http://www.functionvenuefinder.com.au/view_venue/qbb/broadbeach_tavern
http://www.functionvenuefinder.com.au/view_venue/qbr/brook_hotel
http://www.functionvenuefinder.com.au/view_venue/qbd/buderim_tavern
http://www.functionvenuefinder.com.au/view_venue/qbh/burleigh_heads_hotel
http://www.functionvenuefinder.com.au/view_venue/qca/caloundra_hotel
http://www.functionvenuefinder.com.au/view_venue/qcp/capalaba_tavern
http://www.functionvenuefinder.com.au/view_venue/qcc/captain_cook_tavern
http://www.functionvenuefinder.com.au/view_venue/qce/cecil_hotel
http://www.functionvenuefinder.com.au/view_venue/qcy/centenary_tavern
http://www.functionvenuefinder.com.au/view_venue/qcs/chatswood_hills_tavern
http://www.functionvenuefinder.com.au/view_venue/qcg/chermside_tavern
http://www.functionvenuefinder.com.au/view_venue/qcb/club_tavern
http://www.functionvenuefinder.com.au/view_venue/qci/commercial_hotel
http://www.functionvenuefinder.com.au/view_venue/qcu/coutts_commercial_hotel
http://www.functionvenuefinder.com.au/view_venue/qdb/deception_bay_tavern
http://www.functionvenuefinder.com.au/view_venue/qdd/dublin_docks_tavern
http://www.functionvenuefinder.com.au/view_venue/qec/edinburgh_castle_hotel
http://www.functionvenuefinder.com.au/view_venue/qfh/federal_hotel
http://www.functionvenuefinder.com.au/view_venue/qfr/forest_lake_tavern
http://www.functionvenuefinder.com.au/view_venue/qha/hamilton_hotel
http://www.functionvenuefinder.com.au/view_venue/qhf/highfields_tavern
http://www.functionvenuefinder.com.au/view_venue/qhi/hinterland_hotel_motel
http://www.functionvenuefinder.com.au/view_venue/qhl/holland_park_hotel
http://www.functionvenuefinder.com.au/view_venue/qin/indooroopilly_hotel
http://www.functionvenuefinder.com.au/view_venue/qka/kallangur_tavern
http://www.functionvenuefinder.com.au/view_venue/qkw/kawana_waters_hotel
http://www.functionvenuefinder.com.au/view_venue/qkp/kedron_park_hotel
http://www.functionvenuefinder.com.au/view_venue/qke/kensington_junction
http://www.functionvenuefinder.com.au/view_venue/qki/kirwan_tavern
http://www.functionvenuefinder.com.au/view_venue/qlt/lawnton_tavern
http://www.functionvenuefinder.com.au/view_venue/qls/lonestar_tavern
http://www.functionvenuefinder.com.au/view_venue/qmb/melbourne_hotel
http://www.functionvenuefinder.com.au/view_venue/qmm/miami_tavern
http://www.functionvenuefinder.com.au/view_venue/qmo/morrison_hotel
http://www.functionvenuefinder.com.au/view_venue/qmg/mount_gravatt_hotel
http://www.functionvenuefinder.com.au/view_venue/qnm/newmarket_hotel
http://www.functionvenuefinder.com.au/view_venue/qnr/noosa_reef_hotel
http://www.functionvenuefinder.com.au/view_venue/qnf/norfolk_tavern
http://www.functionvenuefinder.com.au/view_venue/qnl/north_lakes_tavern
http://www.functionvenuefinder.com.au/view_venue/qbn/nudgee_beach_hotel
http://www.functionvenuefinder.com.au/view_venue/qof/oxenford_tavern
http://www.functionvenuefinder.com.au/view_venue/qbm/oxford_152
http://www.functionvenuefinder.com.au/view_venue/qox/oxley_tavern
http://www.functionvenuefinder.com.au/view_venue/qpp/pacific_pines_tavern
http://www.functionvenuefinder.com.au/view_venue/qpd/parkwood_tavern
http://www.functionvenuefinder.com.au/view_venue/qpc/pelican_waters_hotel
http://www.functionvenuefinder.com.au/view_venue/qpe/petrie_hotel
http://www.functionvenuefinder.com.au/view_venue/qpw/prince_of_wales_hotel
http://www.functionvenuefinder.com.au/view_venue/qml/pub_mooloolaba
http://www.functionvenuefinder.com.au/view_venue/qrn/raintrees_tavern
http://www.functionvenuefinder.com.au/view_venue/qrb/redbank_plains_tavern
http://www.functionvenuefinder.com.au/view_venue/qre/redland_bay_hotel
http://www.functionvenuefinder.com.au/view_venue/qhr/harvey_road_tavern
http://www.functionvenuefinder.com.au/view_venue/qrx/royal_exchange_hotel
http://www.functionvenuefinder.com.au/view_venue/qry/royal_hotel
http://www.functionvenuefinder.com.au/view_venue/qsm/smithfield_tavern
http://www.functionvenuefinder.com.au/view_venue/qsg/springfield_tavern
http://www.functionvenuefinder.com.au/view_venue/qsp/springwood_hotel
http://www.functionvenuefinder.com.au/view_venue/qsc/stones_corner_hotel
http://www.functionvenuefinder.com.au/view_venue/qsu/sunnybank_hotel
http://www.functionvenuefinder.com.au/view_venue/qsr/surfers_paradise_tavern
http://www.functionvenuefinder.com.au/view_venue/qne/the_edge_hill_tavern
http://www.functionvenuefinder.com.au/view_venue/qct/the_four_mile_creek_hotel
http://www.functionvenuefinder.com.au/view_venue/qga/the_gap_tavern
http://www.functionvenuefinder.com.au/view_venue/qtt/transit_tavern
http://www.functionvenuefinder.com.au/view_venue/qur/upperross_hotel
http://www.functionvenuefinder.com.au/view_venue/qvl/varsity_lakes
http://www.functionvenuefinder.com.au/view_venue/qvp/victoria_point_tavern
http://www.functionvenuefinder.com.au/view_venue/qvy/victory_hotel
http://www.functionvenuefinder.com.au/view_venue/qvi/villa_noosa_hotel
http://www.functionvenuefinder.com.au/view_venue/qwa/warner_tavern
http://www.functionvenuefinder.com.au/view_venue/qwf/waterfront_hotel
http://www.functionvenuefinder.com.au/view_venue/qwh/wharf_tavern
http://www.functionvenuefinder.com.au/view_venue/qwi/wilsonton_hotel
http://www.functionvenuefinder.com.au/view_venue/qwo/woree_tavern
http://www.functionvenuefinder.com.au/view_venue/qwy/wynnum_tavern
http://www.functionvenuefinder.com.au/view_venue/qbp/blue_pacific_hotel
http://www.functionvenuefinder.com.au/view_venue/qmn/magnums_hotel
http://www.functionvenuefinder.com.au/view_venue/qru/russell_tavern
http://www.functionvenuefinder.com.au/view_venue/sar/archer_hotel
http://www.functionvenuefinder.com.au/view_venue/sbb/belgian_beer_cafe
http://www.functionvenuefinder.com.au/view_venue/sez/elizabeth_tavern
http://www.functionvenuefinder.com.au/view_venue/sef/enfield_hotel
http://www.functionvenuefinder.com.au/view_venue/sfi/findon_hotel
http://www.functionvenuefinder.com.au/view_venue/shw/halfway_hotel
http://www.functionvenuefinder.com.au/view_venue/shi/highbury_hotel
http://www.functionvenuefinder.com.au/view_venue/sny/new_york_bar_grill
http://www.functionvenuefinder.com.au/view_venue/sno/norwood_hotel
http://www.functionvenuefinder.com.au/view_venue/spt/playford_tavern
http://www.functionvenuefinder.com.au/view_venue/srg/ramsgate_hotel
http://www.functionvenuefinder.com.au/view_venue/srx/rex_hotel
http://www.functionvenuefinder.com.au/view_venue/ssa/salisbury_hotel
http://www.functionvenuefinder.com.au/view_venue/ssb/seacliff_beach_hotel
http://www.functionvenuefinder.com.au/view_venue/svh/victoria_hotel
http://www.functionvenuefinder.com.au/view_venue/svi/village_hotel
http://www.functionvenuefinder.com.au/view_venue/tch/carlyle_hotel
http://www.functionvenuefinder.com.au/view_venue/tgr/granada_tavern
http://www.functionvenuefinder.com.au/view_venue/tri/riverside_hotel
http://www.functionvenuefinder.com.au/view_venue/tga/gateway_inn_hotel
http://www.functionvenuefinder.com.au/view_venue/vaa/aces_sporting_club
http://www.functionvenuefinder.com.au/view_venue/vbd/bayswater_hotel
http://www.functionvenuefinder.com.au/view_venue/vbi/berwick_inn_hotel
http://www.functionvenuefinder.com.au/view_venue/vbk/blackburn_hotel
http://www.functionvenuefinder.com.au/view_venue/vbn/boundary_hotel
http://www.functionvenuefinder.com.au/view_venue/vbb/braybrook_hotel
http://www.functionvenuefinder.com.au/view_venue/vbv/burvale_hotel
http://www.functionvenuefinder.com.au/view_venue/vch/chelsea_heights_hotel
http://www.functionvenuefinder.com.au/view_venue/vcs/coach_horses
http://www.functionvenuefinder.com.au/view_venue/vcr/coolaroo_hotel
http://www.functionvenuefinder.com.au/view_venue/vcf/cramers_hotel
http://www.functionvenuefinder.com.au/view_venue/vcp/croxton_park_hotel
http://www.functionvenuefinder.com.au/view_venue/vda/daiseys
http://www.functionvenuefinder.com.au/view_venue/vfr/daveys_hotel
http://www.functionvenuefinder.com.au/view_venue/vdp/deer_park_hotel
http://www.functionvenuefinder.com.au/view_venue/vdo/doncaster_hotel
http://www.functionvenuefinder.com.au/view_venue/vet/eltham_hotel
http://www.functionvenuefinder.com.au/view_venue/vft/ferntree_gully_hotel
http://www.functionvenuefinder.com.au/view_venue/vfl/first_last
http://www.functionvenuefinder.com.au/view_venue/vfg/fountain_gate_hotel
http://www.functionvenuefinder.com.au/view_venue/vga/gateway_hotel
http://www.functionvenuefinder.com.au/view_venue/vgl/glengala_hotel
http://www.functionvenuefinder.com.au/view_venue/vha/hallam_hotel
http://www.functionvenuefinder.com.au/view_venue/vhi/highpoint_hotel
http://www.functionvenuefinder.com.au/view_venue/vmj/macs_hotel
http://www.functionvenuefinder.com.au/view_venue/vma/manhattan_hotel
http://www.functionvenuefinder.com.au/view_venue/vmg/manningham_hotel_club
http://www.functionvenuefinder.com.au/view_venue/vmf/matthew_flinders_hotel
http://www.functionvenuefinder.com.au/view_venue/vmi/milanos_tavern
http://www.functionvenuefinder.com.au/view_venue/vmh/mitcham_hotel
http://www.functionvenuefinder.com.au/view_venue/vmo/monash_hotel
http://www.functionvenuefinder.com.au/view_venue/vml/moreland_hotel
http://www.functionvenuefinder.com.au/view_venue/vmn/mountain_view_hotel
http://www.functionvenuefinder.com.au/view_venue/vnu/nu_hotel
http://www.functionvenuefinder.com.au/view_venue/vpa/palace_hotel
http://www.functionvenuefinder.com.au/view_venue/vpv/pascoe_vale_hotel
http://www.functionvenuefinder.com.au/view_venue/vrp/rex_hotel
http://www.functionvenuefinder.com.au/view_venue/vrx/royal_exchange_hotel
http://www.functionvenuefinder.com.au/view_venue/vro/royal_hotel
http://www.functionvenuefinder.com.au/view_venue/vsc/sandbelt_club_hotel
http://www.functionvenuefinder.com.au/view_venue/vsn/sandown_park_hotel
http://www.functionvenuefinder.com.au/view_venue/vsd/sandringham_hotel
http://www.functionvenuefinder.com.au/view_venue/vsa/sands_hotel
http://www.functionvenuefinder.com.au/view_venue/vse/seaford_hotel
http://www.functionvenuefinder.com.au/view_venue/vsh/shoppingtown_hotel
http://www.functionvenuefinder.com.au/view_venue/vsk/skyways_hotel
http://www.functionvenuefinder.com.au/view_venue/vsi/stamford_inn
http://www.functionvenuefinder.com.au/view_venue/vtd/three_degrees
http://www.functionvenuefinder.com.au/view_venue/vsv/vale_hotel
http://www.functionvenuefinder.com.au/view_venue/vve/vegas_-_waverley_gardens
http://www.functionvenuefinder.com.au/view_venue/vvc/victoria_hotel
http://www.functionvenuefinder.com.au/view_venue/vvg/village_green_hotel
http://www.functionvenuefinder.com.au/view_venue/vwm/waltzing_matilda_hotel
http://www.functionvenuefinder.com.au/view_venue/vwp/werribee_plaza_hotel
http://www.functionvenuefinder.com.au/view_venue/vwe/westside_hotel
http://www.functionvenuefinder.com.au/view_venue/vwh/wheelers_hill_hotel
http://www.functionvenuefinder.com.au/view_venue/vyl/york_on_lilydale
http://www.functionvenuefinder.com.au/view_venue/vyj/young_and_jacksons
http://www.functionvenuefinder.com.au/view_venue/vst/st_albans_hotel
http://www.functionvenuefinder.com.au/view_venue/vcm/commercial_hotel
http://www.functionvenuefinder.com.au/view_venue/wbl/balmoral_hotel
http://www.functionvenuefinder.com.au/view_venue/wct/belgian_beer_cafe
http://www.functionvenuefinder.com.au/view_venue/wbm/brass_monkey_hotel
http://www.functionvenuefinder.com.au/view_venue/wbc/bull_creek_tavern
http://www.functionvenuefinder.com.au/view_venue/wid/captain_stirling_hotel
http://www.functionvenuefinder.com.au/view_venue/wcd/como_hotel
http://www.functionvenuefinder.com.au/view_venue/whw/highway_hotel
http://www.functionvenuefinder.com.au/view_venue/whp/hyde_park
http://www.functionvenuefinder.com.au/view_venue/wli/leisure_inn
http://www.functionvenuefinder.com.au/view_venue/wqu/queens_tavern
http://www.functionvenuefinder.com.au/view_venue/wsa/sail_and_anchor
http://www.functionvenuefinder.com.au/view_venue/wst/the_saint_george_hotel
http://www.functionvenuefinder.com.au/view_venue/wbt/the_vic_hotel
http://www.functionvenuefinder.com.au/view_venue/wwv/wanneroo_villa_tavern
http://www.functionvenuefinder.com.au/view_venue/wdu/dunsborough_hotel
http://www.functionvenuefinder.com.au/view_venue/wbk/brooklands_tavern
http://www.functionvenuefinder.com.au/view_venue/wka/kalamunda_hotel
http://www.functionvenuefinder.com.au/view_venue/wcg/carine_glades_tavern
http://www.functionvenuefinder.com.au/view_venue/wbr/brighton_hotel
http://www.functionvenuefinder.com.au/view_venue/wpa/peel_alehouse
http://www.functionvenuefinder.com.au/view_venue/wbe/belmont_tavern
http://www.functionvenuefinder.com.au/view_venue/whl/herdsman_lake_tavern
http://www.functionvenuefinder.com.au/view_venue/wal/albion_hotel
http://www.functionvenuefinder.com.au/view_venue/wgo/gosnells_hotel
http://www.functionvenuefinder.com.au/view_venue/wgr/greenwood_hotel
http://www.functionvenuefinder.com.au/view_venue/wla/lakers_tavern""".split("\n")
 
def print_stuff(link):
    cells = []
    page = urllib2.urlopen(link)
    soup = BeautifulSoup(page)
 
    table = soup.find(id="venue_details_table")
    cells.append(table.thead.tr.td.h3.get_text())
 
    for i, td in enumerate(table.tbody.find_all("td")):
        if i % 2 == 1:
            cells.append(td.get_text())
    print "\t".join(cells)

if __name__ == "__main__":
    for link in links:
        print_stuff(link)
