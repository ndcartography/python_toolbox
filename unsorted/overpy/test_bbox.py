import overpy

api = overpy.Overpass()

# fetch all ways and nodes
result = api.query("""
	[out:json];
    way(50.746,7.154,50.748,7.157) ["highway"];
    (._;>;);
    out body;
    """)
"""    
results = api.query(
	
[out:json];

(
  // get highways
  way[highway!=primary]({{bbox}});
  way[highway!=secondary]({{bbox}});
  way[highway!=tertiary]({{bbox}});
  way[highway!=trunk]({{bbox}});
  
);

out body;
>;
out skel qt;
)
"""

for way in result.ways:
    print("Name: %s" % way.tags.get("name", "n/a"))
    print("  Highway: %s" % way.tags.get("highway", "n/a"))
    print("  Nodes:")
    for node in way.nodes:
        print("    Lat: %f, Lon: %f" % (node.lat, node.lon))