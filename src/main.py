from travel import Travel
import facebook

def convert_date(date):
    return date.split('.')

def main():
    token = 'CAAIsogaCHQ0BAGC4DAqeNoVBFhMGC7hw79DtIqeBLLyikgACzl0WOMTUrvhCLXuEGp5lZCkWFU5F0Aq0JZAvAox3tUAwGbXOmvBc5rxNUOamTFlOR7AVqSmmO9TxZATJVRy24cxhPegpy02yHPlPb0FOZBZC3bcvaLAXnyOvzDvOkc3B8B5h3fw0FgrZC9cjIDIZBIDvaCOv8Ki3PCJSqyAnUitw1ZCpktAZD'
    graph = facebook.GraphAPI(token)
    date = convert_date(raw_input("Date(dd.mm.yy): "))
    destination = raw_input("Destination: ")
    hour = raw_input("Hour(hh.mm): ")
    free_spots = raw_input("Number of free spots: ")
    my_travel = Travel(date[0], date[1], date[2], destination, hour, free_spots)
    my_travel.search_people(graph)
    
if __name__ == '__main__':
    main()