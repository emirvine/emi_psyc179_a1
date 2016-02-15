function [ led1on_times,led2on_times,ledoff_times ] = emi_lights( unique_folder,expkeys )
% requires Nlx2MatEV
% Usage:
% event_id = 10;
% {'TTL Output on AcqSystem1_0 board 0 port 2 value (0x0001).', 'TTL Output on AcqSystem1_0 board 0 port 2 value (0x0002).', 'TTL Output on AcqSystem1_0 board 0 port 2 value (0x0000).'};
% light_idx = emi_lightOn(Timestamps, event_list);
% * Returns light_idx

% fn = FindFile('*Events.nev');
% [EVTimeStamps, ~, ~, ~, EventStrings, ~] = Nlx2MatEV(fn,[1 1 1 1 1],1,1,[]);
% 
% time_convFactor = 10^-6; % converts nlx units to seconds
% 
% ev = unique(EventStrings);
% for i = 1:length(ev);
%     Events(i).type = ev{i};
%     event_index = find(strcmp(EventStrings, Events(i).type));
%     event_times = EVTimeStamps * time_convFactor;
%     Events(i).event_times = event_times(event_index);
%     n_idx = nearest_idx3(Events(i).event_times, Timestamps);
%     Events(i).n_idx = n_idx;
% end
% 
% light_idx = Events(event_id).n_idx;

fn = FindFile('*Events.nev');
[EVTimeStamps, ~, ~, ~, EventStrings, ~] = Nlx2MatEV(fn,[1 1 1 1 1],1,1,[]);

time_convFactor = 10^-6; % converts nlx units to seconds
event_times = EVTimeStamps * time_convFactor;

event_index = strcmp(EventStrings, expkeys.led1id);
led1on_times = event_times(event_index);

event_index = strcmp(EventStrings, expkeys.led2id);
led2on_times = event_times(event_index);

event_index = strcmp(EventStrings, expkeys.ledoff);
ledoff_times = event_times(event_index);

save([unique_folder(1:15),'-pos_event.mat'],'led1on_times','led2on_times','ledoff_times');
end