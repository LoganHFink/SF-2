streams = int(input("Streams:"))

flows = []

for stream in range(streams):
    flows.append(float(input("flow: ")))

done = False

while not done:
    choice = float(input("choice: "))
    if choice == 99: # split
        stream_index = int(input("Stream index: ")) -1
        split_prct = float(input("Split percentage: "))/100
        flows = flows[:stream_index] + [flows[stream_index] * split_prct,flows[stream_index] * (1-split_prct)] + flows[stream_index+1:]
    elif choice == 88: # join
        stream_index = int(input("Stream index: ")) -1
        flows[stream_index] = flows[stream_index] + flows[stream_index+1]
        del flows[stream_index + 1]
    elif choice == 77: # end
        output = ""
        for flow in flows:
            output = output + " " + str(round(flow,1))
        print(output[1:])
        done = True