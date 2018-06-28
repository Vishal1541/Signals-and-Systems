[xn,frate] = audioread('noisy.wav');
len = length(xn);

plot(xn);
title('Noisy Sound');
figure;

win = 20;
g = gausswin(win);
yn = conv(xn,g);

audiowrite('final.wav',yn,frate);
plot(yn);
title('Final Sound');
sound(yn,fs);