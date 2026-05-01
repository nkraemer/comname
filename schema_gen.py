from lxml.etree import Element as Elem
from lxml import etree

root = Elem("COMNAME", version="2025", xmlns="http://ieee.org/c37.232-2025/schema")


# delimiter
delim = Elem("Delimiter")
delim.text = ","
root.append(delim)

# Escape
delim = Elem("EscapeChar")
delim.text = "^"
root.append(delim)

fields = Elem("FileFields")
root.append(fields)

# Time stuff
startdate = Elem("StartDate")
startime = Elem("StartTime")
timecode = Elem("TimeCode")
fields.extend([startdate, startime, timecode])

# stations
station1 = Elem("Station", stationId="1", fullName="My Number 1 Substation")
stations = Elem("Stations")
stations.append(station1)
fields.append(stations)

# devices
device1 = Elem("Device", deviceId="1", fullName="My Number 1 Device")
device2 = Elem("Device", deviceId="two", fullName="My Number two Device")
devices = Elem("Devices")
devices.extend([device1, device2])
fields.append(devices)

# companys
company1 = Elem("Company", companyId="acme", fullName="ACME Inc.")
company2 = Elem(
    "Company",
    companyId="mega",
    fullName="Megacorp",
)
companys = Elem("Companies")
companys.extend([company1, company2])
fields.append(companys)


# Duration
dur = Elem("DurationIso8601")
fields.append(dur)

# Trig type
trig_typ1 = Elem("TrigType", trigTypeId="ag", fullName="A to Ground Fault")
trig_typ2 = Elem("TrigType", trigTypeId="bg", fullName="B to Ground Fault")
trig_typ3 = Elem("TrigType", trigTypeId="cg", fullName="C to Ground Fault")
trig_typ4 = Elem("TrigType", trigTypeId="man", fullName="Manual Trigger")
trig_typs = Elem("TrigTypes")
desc_elem = Elem("Description")
desc_elem.text = "File was manually triggered by a human operator"
trig_typ4.append(desc_elem)
trig_typs.extend([trig_typ1, trig_typ2, trig_typ3, trig_typ4])
fields.append(trig_typs)

# Trig type
data_typs = Elem("DataTypes")
dtypes = {
    "pmu": ("Synchrophasor", "IEEE C37.118-2011.1"),
    "ser": ("Sequence of Event Record", None),
    "raw": ("Raw Unfiltered Data", None),
    "rms": ("RMS Magnitude of Oscillographic Signals", None),
    "dif": ("Differential Protection Data", None),
    "filt": ("Filtered Protection", None),
    "log": ("Log File", None),
    "sv": ("Sampled Values", "IEC 61850-9-2 Sampled Values"),
}
for typ_id, desc in dtypes.items():
    e = Elem("DataType", dataTypeId=typ_id, fullName=desc[0])
    if desc[1]:
        desc_elem = Elem("Description")
        desc_elem.text = desc[1]
        e.append(desc_elem)
    data_typs.append(e)
fields.append(data_typs)

# Geo Location
geo = Elem("GeoLocationIso6709")
fields.append(geo)

# Generic
gen1 = Elem("Generic", genericType="favColour")
desc = Elem("Description")
desc.text = "Favourite Colour of the comissioning team"
gen1.append(desc)
fields.append(gen1)

folders = Elem("Folders")
company_cat = Elem("Category")
gen = Elem("GenericField", genericType="favColour")
company = Elem("Company")
company_cat.extend([company, gen])
date_cat = Elem("Category")
date_cat.append(Elem("ccyymm"))
folders.extend([company_cat, date_cat])
root.append(folders)

# private
private_elem = Elem(
    "SamplePrivateElement", xmlns="http://megacorp.com/unique_namespace"
)
root.append(private_elem)


with open("schema.xml", "w") as f:
    f.write(etree.tostring(root, encoding="unicode", pretty_print=True))

print("schema written")
