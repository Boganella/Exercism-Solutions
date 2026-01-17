<?php

class Lasagna
{
    public function expectedCookTime()
    {
        return 40;
    }

    public function remainingCookTime($elapsed_minutes)
    {
        $remainder = $this->expectedCookTime() - $elapsed_minutes;
        return $remainder;
    }

    public function totalPreparationTime($layers_to_prep)
    {
        $prep_time = $layers_to_prep * 2;
        return $prep_time;
    }

    public function totalElapsedTime($layers_to_prep, $elapsed_minutes)
    {
        $total_time = $this->totalPreparationTime($layers_to_prep) + $elapsed_minutes;
        return $total_time;
    }

    public function alarm()
    {
        return "Ding!";
    }
}
