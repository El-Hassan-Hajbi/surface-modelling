close all; clear all;

    B1 = load("c1_herisson.txt");
    B2 = load("c2_main.txt");
    B3 = load("c3_chien.txt");
    B4 = load("c4_avion.txt");
    B5 = load("c5_requin.txt");
    B6 = load("c6_poisson.txt");
    B7 = load("c7_seahorse.txt");
    figure; axis equal;
    plot(B1(:,1), B1(:, 2), 'k-');
    figure; axis equal;
    plot(B2(:,1), B2(:, 2), 'k-');
    figure; axis equal;
    plot(B3(:,1), B3(:, 2), 'k-');
    figure; axis equal;
    plot(B4(:,1), B4(:, 2), 'k-');
    figure; axis equal;
    plot(B5(:,1), B5(:, 2), 'k-');
    figure; axis equal;
    plot(B6(:,1), B6(:, 2), 'k-');
    figure; axis equal;
    plot(B7(:,1), B7(:, 2), 'k-');
