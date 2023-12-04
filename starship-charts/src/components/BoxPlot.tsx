import * as React from 'react';
import { ResponsiveBoxPlot } from '@nivo/boxplot'
import { fetchStarshipCostsByFilm } from '../services/swapiService.ts';

export default function BoxPlot () {
    const [chartData, setChartData] = React.useState<any>([]);
    React.useEffect(() => {
      (async () => {
          const data = await fetchStarshipCostsByFilm();
          setChartData(data);
          console.log(data);
      })()
    }, []);
    return (
        <ResponsiveBoxPlot
            data={chartData}
            margin={{ top: 60, right: 140, bottom: 60, left: 60 }}
            padding={0.12}
            enableGridX={true}
            axisTop={{
                tickSize: 5,
                tickPadding: 5,
                tickRotation: 0,
                legend: '',
                legendOffset: 36
            }}
            axisRight={{
                tickSize: 5,
                tickPadding: 5,
                tickRotation: 0,
                legend: '',
                legendOffset: 0
            }}
            axisBottom={{
                tickSize: 5,
                tickPadding: 5,
                tickRotation: 0,
                legend: 'group',
                legendPosition: 'middle',
                legendOffset: 32
            }}
            axisLeft={{
                tickSize: 5,
                tickPadding: 5,
                tickRotation: 0,
                legend: 'value',
                legendPosition: 'middle',
                legendOffset: -40
            }}
            colors={{ scheme: 'nivo' }}
            borderRadius={2}
            borderWidth={2}
            borderColor={{
                from: 'color',
                modifiers: [
                    [
                        'darker',
                        0.3
                    ]
                ]
            }}
            medianWidth={2}
            medianColor={{
                from: 'color',
                modifiers: [
                    [
                        'darker',
                        0.3
                    ]
                ]
            }}
            whiskerEndSize={0.6}
            whiskerColor={{
                from: 'color',
                modifiers: [
                    [
                        'darker',
                        0.3
                    ]
                ]
            }}
            motionConfig="stiff"
            legends={[
                {
                    anchor: 'right',
                    direction: 'column',
                    justify: false,
                    translateX: 100,
                    translateY: 0,
                    itemWidth: 60,
                    itemHeight: 20,
                    itemsSpacing: 3,
                    itemTextColor: '#999',
                    itemDirection: 'left-to-right',
                    symbolSize: 20,
                    symbolShape: 'square',
                    effects: [
                        {
                            on: 'hover',
                            style: {
                                itemTextColor: '#000'
                            }
                        }
                    ]
                }
            ]}
        />
    );
}